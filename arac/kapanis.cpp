// Önerme kapanışı: verilen kök bildirimlerin "ne söylediğini" anlamak için gereken bildirimler.
// Teoremlerde yalnızca tip (önerme) izlenir, ispat izlenmez; tanım/tip/yapılarda her şey izlenir.
// Kullanım: kapanis gecici.bin cikti_klasoru kok1.txt [kok2.txt ...] < kayit.ndjson   (kökler: satır başına bir tam ad)
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;
static const uint32_t LEAF=0xFFFFFFFEu, CONST=0xFFFFFFFFu, NAMEF=0x80000000u;
static long gi(const char* s,const char* k){ const char* p=strstr(s,k); if(!p) return -1; return strtol(p+strlen(k),nullptr,10); }
struct Decl{ uint64_t pos; char kind; vector<uint32_t> names, exprs; };
int main(int argc,char**argv){
  if(argc<4){ fprintf(stderr,"kullanim\n"); return 1; }
  uint64_t CAP=getenv("KUNYE_KAPASITE")?strtoull(getenv("KUNYE_KAPASITE"),nullptr,10):2100000000ULL;
  int fd=open(argv[1],O_RDWR|O_CREAT|O_TRUNC,0644); if(ftruncate(fd,CAP*8)){perror("ft");return 1;}
  uint32_t* E=(uint32_t*)mmap(nullptr,CAP*8,PROT_READ|PROT_WRITE,MAP_SHARED,fd,0);
  unordered_map<uint32_t,uint32_t> third;
  vector<Decl> D; vector<uint32_t> npre{0}; vector<uint32_t> noff{0}; string nbuf;
  uint64_t ne=0; char* buf=nullptr; size_t cap=0; ssize_t n;
  while((n=getline(&buf,&cap,stdin))>0){
    const char* s=buf;
    if(s[2]=='i'&&s[3]=='n'&&s[4]=='"'){
      long pre=gi(s,"\"pre\":"); const char* q=strstr(s,"\"str\":\""); string nm;
      if(q){ q+=7; const char* e=strchr(q,'"'); nm.assign(q,e-q);} else nm="#"+to_string(gi(s,"\"i\":"));
      npre.push_back((uint32_t)pre); nbuf+=nm; noff.push_back(nbuf.size()); continue;
    }
    if(s[2]=='i'&&s[3]=='l'&&s[4]=='"') continue;
    const char* ie=strstr(s,"\"ie\":");
    if(ie){
      uint32_t a=LEAF,b=LEAF; long id=strtol(ie+5,nullptr,10);
      if(strstr(s,"\"app\":{")){ a=gi(s,"\"fn\":"); b=gi(s,"\"arg\":"); }
      else if(strstr(s,"\"lam\":{")||strstr(s,"\"forallE\":{")){ a=gi(s,"\"type\":"); b=gi(s,"\"body\":"); }
      else if(strstr(s,"\"const\":{")){ a=CONST; b=gi(s,"\"name\":"); }
      else if(strstr(s,"\"letE\":{")){ a=gi(s,"\"type\":"); b=gi(s,"\"value\":"); third[id]=gi(s,"\"body\":"); }
      else if(strstr(s,"\"proj\":{")){ a=gi(s,"\"struct\":"); b=NAMEF|(uint32_t)gi(s,"\"typeName\":"); }
      else if(strstr(s,"\"mdata\":{")){ a=gi(s,"\"expr\":"); }
      E[2*ne]=a; E[2*ne+1]=b; ne++; continue;
    }
    if(!strncmp(s,"{\"meta\"",7)) continue;
    Decl d; d.pos=ne; d.kind=s[2];
    const char* p=s;
    while((p=strchr(p,'"'))){
      const char* k=p+1; const char* ke=strchr(k,'"'); if(!ke)break; size_t kl=ke-k; p=ke+1;
      if(*p!=':') continue; p++; if(*p<'0'||*p>'9') continue;
      long v=strtol(p,nullptr,10);
      if(kl==4&&!strncmp(k,"name",4)) d.names.push_back(v);
      else if((kl==4&&!strncmp(k,"type",4))||(kl==5&&!strncmp(k,"value",5))||(kl==3&&!strncmp(k,"rhs",3))) d.exprs.push_back(v);
    }
    D.push_back(move(d));
  }
  size_t NN=npre.size();
  fprintf(stderr,"ifade %lu isim %zu bildirim %zu\n",ne,NN,D.size());
  auto full=[&](uint32_t x){ string r; while(x){ string part=nbuf.substr(noff[x-1],noff[x]-noff[x-1]); r=r.empty()?part:part+"."+r; x=npre[x]; } return r; };
  vector<int32_t> declOf(NN,-1);
  for(size_t i=0;i<D.size();i++) for(auto x:D[i].names) if(x<NN&&declOf[x]<0) declOf[x]=i;
  unordered_map<string,uint32_t> byname;
  for(size_t i=0;i<D.size();i++) for(auto x:D[i].names) if(x<NN) byname.emplace(full(x),x);
  for(int a=3;a<argc;a++){
    vector<uint32_t> roots; FILE* rf=fopen(argv[a],"r"); char lb[8192];
    while(fgets(lb,sizeof lb,rf)){ string s(lb); while(!s.empty()&&(s.back()=='\n'||s.back()=='\r')) s.pop_back(); auto it=byname.find(s); if(it!=byname.end()) roots.push_back(it->second); else fprintf(stderr,"bulunamadi: %s\n",s.c_str()); }
    fclose(rf);
    vector<bool> needE(ne,false), needN(NN,false), reached(D.size(),false);
    for(auto r:roots) needN[r]=true;
    uint64_t late; int pass=0;
    auto procD=[&](long j){ Decl&d=D[j]; bool nd=false; for(auto x:d.names) if(x<NN&&needN[x]) nd=true; if(!nd) return; reached[j]=true;
      for(auto x:d.names) if(x<NN) needN[x]=true;
      bool yard=false; if(d.kind=='t'&&!d.names.empty()&&d.names[0]<NN){ uint32_t x=d.names[0]; yard=nbuf[noff[x-1]]=='_'; }
      if(d.kind=='t'&&!yard){ if(!d.exprs.empty()&&d.exprs[0]<ne) needE[d.exprs[0]]=true; }  // teorem: yalnızca önerme (yardımcı _proof_N teoremlerinin değeri de)
      else for(auto x:d.exprs) if(x<ne) needE[x]=true; };
    do{ late=0; pass++; long j=(long)D.size()-1;
      for(int64_t e=(int64_t)ne-1;e>=0;e--){
        while(j>=0&&D[j].pos>(uint64_t)e){ procD(j); j--; }
        if(!needE[e]) continue;
        uint32_t x=E[2*e], y=E[2*e+1];
        if(x==CONST){ if(y<NN&&!needN[y]){ needN[y]=true; if(declOf[y]>j) late++; } continue; }
        if(x!=LEAF&&x<ne) needE[x]=true;
        if(y!=LEAF){ if(y&NAMEF){ uint32_t z=y&~NAMEF; if(z<NN&&!needN[z]){ needN[z]=true; if(declOf[z]>j) late++; } } else if(y<ne) needE[y]=true; }
        auto it=third.find(e); if(it!=third.end()) needE[it->second]=true;
      }
      while(j>=0){ procD(j); j--; }
    } while(late>0&&pass<30);
    string out=string(argv[2])+"/"+string(strrchr(argv[a],'/')?strrchr(argv[a],'/')+1:argv[a])+".kapanis";
    FILE* o=fopen(out.c_str(),"w"); uint64_t c=0;
    for(size_t i=0;i<D.size();i++) if(reached[i]&&!D[i].names.empty()){ fprintf(o,"%c\t%s\n",D[i].kind,full(D[i].names[0]).c_str()); c++; }
    fclose(o);
    fprintf(stderr,"%s: kok %zu, gereken bildirim %lu (%d tur)\n",argv[a],roots.size(),c,pass);
  }
  return 0;
}

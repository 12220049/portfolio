from pathlib import Path
import svgwrite,base64,textwrap
ROOT=Path(__file__).resolve().parent
PHOTO=(ROOT.parent/'assets/novin-rai-portrait.jpg').read_bytes();PH='data:image/jpeg;base64,'+base64.b64encode(PHOTO).decode()
NAVY='#15283C';BLUE='#235A97';GOLD='#B8884F';MUTED='#61758A';PALE='#F6F8FA';BORDER='#DCE5ED';WHITE='#FFFFFF'
class Art:
 def __init__(self,name,w,h,low=False):
  self.d=svgwrite.Drawing(str(ROOT/name),size=(w,h),viewBox=f'0 0 {w} {h}',profile='full');self.w=w;self.h=h;self.low=low;self.d.add(self.d.rect(insert=(0,0),size=(w,h),fill='#F4F4F4' if low else 'white'))
 def rect(self,x,y,w,h,fill=WHITE,r=0,stroke=None,sw=1):self.d.add(self.d.rect(insert=(x,y),size=(w,h),rx=r,ry=r,fill=fill,stroke=stroke or 'none',stroke_width=sw))
 def ln(self,x1,y1,x2,y2,c=BORDER,wd=1):self.d.add(self.d.line(start=(x1,y1),end=(x2,y2),stroke=c,stroke_width=wd))
 def circ(self,x,y,r,fill):self.d.add(self.d.circle(center=(x,y),r=r,fill=fill))
 def text(self,s,x,y,size=19,weight=400,color=NAVY,family='Arial',letter=0):self.d.add(self.d.text(s,insert=(x,y),font_size=size,font_weight=weight,fill=color,font_family=family,letter_spacing=letter))
 def labels(self,strings,x,y,size=17,spacing=28,color=MUTED,weight=400):
  for i,line in enumerate(strings):self.text(line,x,y+i*spacing,size,weight,color)
 def save(self):self.d.save();print(self.d.filename)
def navbar(a,wide=True,low=False):
 w=a.w;a.rect(0,0,w,76,fill='#EFEFEF' if low else WHITE);a.ln(0,75,w,75,'#D3D3D3' if low else BORDER)
 if low:a.rect(60,24,40,29,'#B9B9B9',5);a.rect(112,32,112,10,'#B9B9B9',2)
 else:a.rect(55,17,40,40,NAVY,8);a.text('NR',64,44,17,800,WHITE);a.text('Novin Rai',109,43,20,800)
 if wide:
  for i,v in enumerate(['Home','About','Expertise','Work','Case Studies','Design']):a.text(v,w-560+i*82,43,12,700,('#8C8C8C' if low else MUTED))
def low_home_desktop():
 a=Art('low_home_desktop.svg',1440,1890,True);navbar(a)
 a.rect(0,76,1440,590,'#E7E7E7');a.rect(72,148,190,18,'#BBBBBB',3)
 a.rect(72,209,560,62,'#AAAAAA',4);a.rect(72,288,462,58,'#B4B4B4',4)
 for i,l in enumerate([525,495,450]):a.rect(72,386+i*34,l,14,'#C1C1C1',3)
 a.rect(72,525,160,46,'#A9A9A9',7);a.rect(247,525,155,46,'#D3D3D3',7,stroke='#B7B7B7');a.rect(848,135,455,490,'#C9C9C9',210);a.text('PORTRAIT IMAGE',959,407,20,700,'#858585')
 a.rect(0,666,1440,120,'#D1D1D1');[a.rect(100+445*i,700,300,52,'#B7B7B7',6) for i in range(3)]
 a.text('ABOUT / EDUCATION',72,849,20,700,'#777');a.rect(72,890,520,46,'#A7A7A7',5)
 for i,l in enumerate([550,500,540,420]):a.rect(72,964+i*32,l,14,'#C3C3C3',3)
 a.rect(800,840,546,270,'#E4E4E4',13,stroke='#C6C6C6');a.rect(831,877,240,18,'#B8B8B8',3);a.rect(831,925,442,25,'#B0B0B0',4)
 a.text('SKILLS / CAPABILITIES',72,1190,20,700,'#777')
 for i in range(3):
  x=72+i*435;a.rect(x,1241,412,202,WHITE,10,stroke='#C7C7C7');a.rect(x+25,1274,212,21,'#B5B5B5',3)
  for j in range(3):a.rect(x+25,1326+j*31,290,13,'#D0D0D0',3)
 a.text('PROJECT CASE STUDIES',72,1530,20,700,'#777')
 for i in range(4):
  x=72+i*328;a.rect(x,1583,307,248,WHITE,12,stroke='#C6C6C6');a.rect(x+15,1598,277,115,'#C6C6C6',6);a.rect(x+18,1740,196,16,'#B4B4B4',4);a.rect(x+18,1781,241,11,'#CECECE',4)
 a.save()
def low_home_mobile():
 a=Art('low_home_mobile.svg',390,2000,True);a.rect(0,0,390,65,'#EFEFEF');a.rect(18,18,36,30,'#B0B0B0',5);a.rect(64,28,103,10,'#B9B9B9',3);a.rect(346,23,26,22,'#B6B6B6',3)
 a.rect(0,65,390,535,'#E5E5E5');a.rect(24,107,150,13,'#B7B7B7',3);a.rect(24,159,323,45,'#A7A7A7',3);a.rect(24,219,265,44,'#AFAFAF',3)
 for i,l in enumerate([315,305,271]):a.rect(24,294+i*27,l,12,'#C3C3C3',3)
 a.rect(24,399,140,42,'#A5A5A5',6);a.rect(176,399,140,42,'#D0D0D0',6)
 a.rect(90,461,218,139,'#BEBEBE',90);a.text('PHOTO',165,535,14,700,'#777')
 a.rect(0,600,390,90,'#D2D2D2');a.rect(24,620,152,45,'#B7B7B7',5);a.rect(193,620,173,45,'#B7B7B7',5)
 a.text('ABOUT',24,740,16,700,'#777');a.rect(24,772,250,28,'#B6B6B6',4)
 for i,l in enumerate([338,320,312,235]):a.rect(24,822+i*27,l,12,'#C6C6C6',3)
 a.rect(24,957,342,180,'#E5E5E5',10,stroke='#C6C6C6');a.rect(42,981,246,18,'#B4B4B4',4)
 a.text('SKILLS',24,1190,16,700,'#777')
 for i in range(3):a.rect(24,1224+i*121,342,103,WHITE,10,stroke='#C6C6C6');a.rect(42,1243+i*121,230,17,'#B7B7B7',3);a.rect(42,1279+i*121,278,12,'#D1D1D1',3)
 a.text('PROJECTS',24,1645,16,700,'#777')
 for i in range(2):a.rect(24,1681+i*145,342,128,WHITE,9,stroke='#C6C6C6');a.rect(36,1693+i*145,111,102,'#C9C9C9',6);a.rect(164,1716+i*145,170,16,'#B2B2B2',4)
 a.save()
def low_case_desktop():
 a=Art('low_case_desktop.svg',1440,1180,True);navbar(a);a.rect(0,76,1440,334,'#E6E6E6');a.rect(72,134,250,16,'#B8B8B8',3);a.rect(72,192,604,50,'#A9A9A9',5)
 for i,l in enumerate([603,532,460]):a.rect(72,273+i*27,l,12,'#C2C2C2',3)
 a.rect(901,116,458,265,'#C2C2C2',10)
 a.rect(73,469,215,650,'#F2F2F2',8,stroke='#D0D0D0')
 for i in range(6):a.rect(96,504+i*66,160,14,'#C3C3C3',3)
 a.rect(332,473,420,44,'#A7A7A7',4)
 for i,l in enumerate([980,925,998,865]):a.rect(332,552+i*31,l,13,'#C7C7C7',3)
 for i in range(3):a.rect(332+i*346,747,322,212,'#E7E7E7',10,stroke='#C5C5C5')
 a.save()
def high_home_desktop():
 a=Art('high_home_desktop.svg',1440,1890);navbar(a)
 a.rect(0,76,1440,660,'#F1F5F9');a.rect(74,159,239,31,WHITE,15,stroke=BORDER);a.text('GCIT  ·  4TH YEAR',91,180,12,700,BLUE)
 a.text('ARTIFICIAL INTELLIGENCE  /  DATA SCIENCE',74,241,13,800,BLUE,letter=1.3)
 a.text("Hi, I'm",74,321,69,800,NAVY);a.text('Novin Rai.',74,405,77,800,BLUE);a.text('I build with purpose.',74,490,59,800,NAVY)
 a.labels(['AI & Data Science student at Gyalpozhing College of','Information Technology. Exploring useful software and','thoughtful machine-learning applications.'],74,551,19,31,MUTED)
 a.rect(74,657,193,54,BLUE,8);a.text('Explore my work  ↗',94,691,16,700,WHITE)
 a.rect(281,657,188,54,WHITE,8,stroke=BORDER);a.text('Read case studies',297,691,15,700,NAVY)
 a.rect(878,130,451,606,'#DCE6EF',225);a.d.add(a.d.image(href=PH,insert=(900,157),size=(410,579),preserveAspectRatio='xMidYMin slice'));a.rect(853,661,260,57,WHITE,4,stroke=BORDER);a.text('Novin Rai',870,686,15,800,NAVY);a.text('AI / DATA SCIENCE · GCIT',870,704,10,500,MUTED)
 a.rect(0,736,1440,123,NAVY)
 for i,(n,t) in enumerate([('04','PROJECTS'),('FULL-STACK','ENGINEERING'),('4TH YEAR','GCIT')]):
  x=83+i*430;a.text(n,x,792,26,800,WHITE);a.text(t,x,817,11,700,'#ACC0D3',letter=1.4)
 a.text('01 / ABOUT',74,949,13,800,BLUE,letter=2);a.text('Engineering curiosity',74,1001,44,800,NAVY);a.text('into useful work.',74,1056,44,800,NAVY)
 a.labels(['I am a fourth-year AI and Data Science student at','Gyalpozhing College of Information Technology. My','interests span AI, data analysis and software engineering.'],74,1112,18,34,MUTED)
 a.rect(789,920,568,292,'#F1F5F9',15,stroke=BORDER);a.rect(818,947,72,5,GOLD,3);a.text('EDUCATION',818,994,13,800,BLUE,letter=1.5);a.text('Gyalpozhing College of',818,1040,25,800,NAVY);a.text('Information Technology',818,1076,25,800,NAVY);a.text('4th Year   /   AI & Data Science',818,1124,17,500,MUTED)
 a.rect(0,1275,1440,615,'#F6F8FA');a.text('02 / SELECTED WORK',74,1363,13,800,BLUE,letter=2);a.text('Projects with real questions.',74,1420,42,800,NAVY)
 projects=[('Blood Group Detection AI','Fingerprint-based AI exploration','#DCE9F4'),('DanceTutor','Bhutanese cultural dance & AI','#E7ECEF'),('Deforestation Detection','AI for forest-cover changes','#E2EBE6'),('Dzen AI','Dzongkha / English LLM MCQs','#E7EAF3')]
 for i,(title,desc,bg) in enumerate(projects):
  x=74+(i%2)*652;y=1471+(i//2)*201;a.rect(x,y,618,179,WHITE,12,stroke=BORDER);a.rect(x+16,y+17,183,145,bg,10)
  a.text(f'0{i+1} / CASE STUDY',x+217,y+46,12,800,GOLD,letter=1);a.text(title,x+217,y+83,23,800,NAVY);a.text(desc,x+217,y+111,14,400,MUTED);a.text('Explore  ↗',x+217,y+146,13,800,BLUE)
 a.save()
def high_home_mobile():
 a=Art('high_home_mobile.svg',390,1940);a.rect(0,0,390,65,WHITE);a.ln(0,64,390,64,BORDER);a.rect(18,14,38,38,NAVY,7);a.text('NR',25,39,15,800,WHITE);a.text('Novin Rai',68,38,17,800,NAVY);a.text('☰',347,39,23,700,NAVY)
 a.rect(0,65,390,660,'#F1F5F9');a.text('GCIT  ·  4TH-YEAR STUDENT',22,115,12,800,BLUE,letter=1)
 a.text("Hi, I'm",22,179,42,800,NAVY);a.text('Novin Rai.',22,229,44,800,BLUE);a.text('I build with',22,280,44,800,NAVY);a.text('purpose.',22,331,44,800,NAVY)
 a.labels(['AI & Data Science at Gyalpozhing College','of IT. Building thoughtful software and','exploring intelligent systems.'],22,375,15,26,MUTED)
 a.rect(22,469,165,42,BLUE,8);a.text('Explore work ↗',38,496,13,800,WHITE);a.rect(197,469,164,42,WHITE,8,stroke=BORDER);a.text('Case studies',220,496,13,800,NAVY)
 a.rect(73,544,244,181,'#DDE6EF',110);a.d.add(a.d.image(href=PH,insert=(102,551),size=(190,174),preserveAspectRatio='xMidYMin slice'))
 a.rect(0,725,390,116,NAVY);a.text('04',22,771,23,800,WHITE);a.text('PROJECTS',22,792,10,700,'#B6C6D7');a.text('4TH YEAR',200,771,21,800,WHITE);a.text('GCIT',200,792,10,700,'#B6C6D7')
 a.text('01 / ABOUT',22,893,12,800,BLUE);a.text('Engineering curiosity',22,932,25,800,NAVY);a.text('into useful work.',22,961,25,800,NAVY)
 a.labels(['AI & Data Science student at GCIT,','working across software engineering,','cultural technology and data-driven AI.'],22,1003,14,25,MUTED)
 a.rect(22,1102,346,179,'#F1F5F9',10,stroke=BORDER);a.text('EDUCATION',42,1139,12,800,BLUE);a.text('Gyalpozhing College of',42,1174,19,800,NAVY);a.text('Information Technology',42,1201,18,800,NAVY);a.text('4th Year · AI & Data Science',42,1240,13,400,MUTED)
 a.rect(0,1312,390,628,'#F6F8FA');a.text('02 / SELECTED WORK',22,1366,12,800,BLUE);a.text('Selected projects',22,1404,28,800,NAVY)
 for i,(title,desc) in enumerate([('Blood Group Detection AI','Fingerprint-based AI research'),('DanceTutor','Bhutanese cultural dance AI'),('Deforestation Detection','Image-based change analysis'),('Dzen AI','Bilingual LLM comparison')]):
  y=1435+119*i;a.rect(22,y,346,103,WHITE,9,stroke=BORDER);a.rect(36,y+13,73,76,'#E5ECF3',7);a.text(f'0{i+1}',55,y+59,24,800,BLUE);a.text(title,125,y+38,16,800,NAVY);a.text(desc,125,y+63,11,400,MUTED)
 a.save()
def high_case_desktop():
 a=Art('high_case_desktop.svg',1440,1190);navbar(a)
 a.rect(0,76,1440,376,'#F1F5F9');a.text('HOME  /  CASE STUDIES  /  BLOOD GROUP DETECTION',67,133,12,700,BLUE,letter=1)
 a.text('CASE STUDY 01  /  EXPLORATORY AI',67,198,13,800,GOLD,letter=1.3);a.text('Blood Group',67,265,56,800,NAVY);a.text('Detection AI',67,334,56,800,NAVY)
 a.labels(['Exploring fingerprint features for experimental blood-group','classification. Not a replacement for verified medical testing.'],67,374,18,27,MUTED)
 a.rect(900,115,465,276,NAVY,14)
 for i in range(5):
  x=1085;y=255
  a.d.add(a.d.path(d=f'M {x-100+i*17},{y+84} Q {x-118+i*20},{y-104+i*12} {x+8-i*6},{y-84+i*13} Q {x+125-i*22},{y-56} {x+102-i*11},{y+85}',fill='none',stroke='#91BDE6',stroke_width=3))
 a.rect(67,503,220,617,'#F8FAFC',13,stroke=BORDER)
 for i,label in enumerate(['Overview','Problem & goal','Approach','System flow','Decisions','Next steps']):a.text(label,85,553+i*73,15,700,MUTED)
 a.text('01 / OVERVIEW',335,532,13,800,BLUE,letter=1.5);a.text('At a glance',335,588,43,800,NAVY)
 a.labels(['An exploratory project investigating whether fingerprint-image','patterns can help predict a blood-group category in a study','dataset. Validation is essential before making any claims.'],335,638,19,32,MUTED)
 a.rect(335,762,502,294,'#F8FAFC',13,stroke=BORDER);a.text('THE CHALLENGE',363,811,13,800,BLUE);a.labels(['Blood typing is normally established','with laboratory testing. Fingerprint-','based prediction remains experimental.'],363,859,18,32,NAVY)
 a.rect(854,762,501,294,'#F8FAFC',13,stroke=BORDER);a.text('PROJECT GOAL',882,811,13,800,BLUE);a.labels(['Investigate classification signals,','quantify limitations and evaluate','the model responsibly.'],882,859,18,32,NAVY)
 a.save()
low_home_desktop();low_home_mobile();low_case_desktop();high_home_desktop();high_home_mobile();high_case_desktop()

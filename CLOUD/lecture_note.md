# Cloud Computing

## 클라우드 컴퓨팅의 논리적 3계층
- IaaS : Infrastructure as a Service / 가상 컴퓨터 스토리지 네트워크
- PaaS : Platform as a Service / 응용 프로그램의 개발을 돕는 플랫폼
- SaaS : Software as a Service / 사용자에게 제공되는 소프트웨어 또는 서비스를 가상화하여 제공

## 그 외 계층(XaaS)
- BaaS(Backend as a Service), FaaS(Function as a Service), CaaS(Container as a Service), SECaaS(Security as a Service)
- FaaS : 서버리스 아키텍처 구성을 위한 서비스 ➡️ AWS Lambda, Azure Functions
- CaaS : 컨테이너 환경을 위한 서비스 ➡️ AWS EKS, AWS ECS, AWS Fargate...

## 서비스 유형
- 퍼블릭 클라우드 : 클라우드 공급자(CSP)에게 제공받아 쓰는 방식
- 프라이빗 클라우드 : 단일 비즈니스 또는 조직에서 독점적으로 제공되는 서비스
- 하이브리드 클라우드

## 하이퍼바이저(Hypervisor)
- 가상머신(Virtual Machine, VM)을 생성하고 구독하는 소프트웨어
- 가상머신모니터(Virtual Machine Monitor, VMM)라고 불림
- 운영체제와 가상 머신의 리소스를 분리해 VM의 생성과 관리를 지원
- 오래전부터 있던 기술!

## 클라우드 컴퓨팅 서비스 프로바이더
- 글로벌 벤더 : AWS / Azure / GCP...

## AWS 보안 : 공동 책임 모델(Separation of Responsibilities)
- AWA 책임 '클라우드의 보안' : PaaS / SaaS
- 고객 책임 '클라우드에서의 보안' : On-Premisese / IaaS / 데이터 활용 레벨

## AWS 서버 격리(Instance Isolation)
- DOD(미국 국방부) / NIST 표준 준수

## SLA(Service Level Agreement) : 사용자 약관
- AWS 클라우드 서비스의 안정성은 SLA 99.95%로 정의되어 있다(평균적 수치 / 실제로는 서비스마다 다름)
- 0.05%의 장애가 발생할 수 있다
- ➡️ 장애가 발생해도 괜찮도록 설계해야 한다❗️

## AWS 구축 절차
- VPC : AWS 클라우드 내 구축하는 가상의 네트워크 영역(데이터센터)
- VPN : On-prem 데이터 센터와 VPC 간에 VPN(IPSec) 연결
- Direct Connect : On-prem 데이터 센터와 VPC의 전용선 연결
- ELB : 관리형 Load Balancer 서비스
- Route 53 : 관리형 DNS 서비스

## 가용 영역(Availability Zone)

## AWS 보안 아키텍처 구현 기본 요소
- 멀티 레이어 보안 아키텍처를 통한 다차원 대응
- 사용자 보안 : IAM - 클라우드 보안의 기본 요소, 사용자 계정 관리
  - 인증 / 보안 상식 ✨
  - Multi-factor Authentiacation(MFA) : Knowledge(Type1) / Possession(Type2) / Biometric(Type3)
  - MFA의 기본은 다른 타입 두 가지를 합치는 것!
- 네트워크 보안 : VPC : 사용자 정의 가능한 논리적 네트워크 환경
  - 접근 제어
    - SG(Security Group / 인스턴스 보안 / 방화벽 / 기본 차단)
    - ACL(Access Control List / 네트워크 보안 / NACL(Network ~) / 차단 목적 / 기본 허용 : 모든 차단은 SG에서 해주기 때문에)
  - 가용성
    - AS(Auto-Scaling / 이중화)
- 서버 보안 : SG, EC2(linux)
- 서비스 보안 : (nginx)
- 가용성 : Route53, ELB, AutoScaling

## VPC 설정을 위한 네트워크 101 복습❗️ - [IPv4 주소 체계](https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/jsp/resources/ipv4Info.jsp)
- [✨ RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)
- IP(Internet Protocol) : **고유한** 서버의 주소
- IPv4 : 32비트 주소 체계 ➡️ 0.0.0.0 ~ 255.255.255.255 ➡️ 약 42억개
  - class A / B / C / D / E
  - 네트워크 대역 : 서브넷(subnet) / 서브넷 마스크
  - 클래스 16 / 클래스 24... 1의 개수로 표시하기도 함
  - 네트워크 아이디(고정값) / 호스트 아이디(가변)
  - 공인 IP / 사설 IP 체계
    - 클래스 별로 사설 IP 대역이 있음 : class A - 10.0.0.0 / B - 172.16.0.0 / C - 192.168.0.0...
  - Special 대역도 있다
- IPv6 : IPv4의 고갈로 모바일은 IPv6 ➡️ 128비트 주소 체계

## Lightsail
- 기술 지식이 제한된 사람들도 쉽게 사용할 수 있도록 설계됨

~~~shell
cd stack
cd nginx/html
echo "<h1> Welcome to LightSail from mjkim </h1>" > index.html
~~~

### 내 터미널에서 원격 서버에 접속 : ssh(secure shell)
- ssh <계정명>@<서버IP>
- ssh -i <키파일> <계정명>@<서버IP>
- Bitnami (nginx 웹서버를 만든 회사 이름) / LAMP(Linux + Apahche + MySQL + PHP)
- 클라우드에서는 id/pw(Type1) 사용하지 않음 : 보안에 취약하기 때문에 Type2를 이용해서 인증함 / .pem : 개인키 파일 확장자 ➡️ compromised 된 키는 폐기해야 함

~~~zsh
chmod 600 LightsailDefaultKey-ap-northeast-2.pem
# 파일 복사하기 / 복사할 파일이 있는 폴더 안에서!
scp -i ~/downloads/LightsailDefaultKey-ap-northeast-2.pem hello.py bitnami@3.35.0.6:/home/bitnami
# scp -r(recursive)
# 폴더 통째로 복사하기 / 복사할 폴더 안에서!
scp -r -i ~/downloads/LightsailDefaultKey-ap-northeast-2.pem . bitnami@3.35.0.6:/home/bitnami
ssh -i LightsailDefaultKey-ap-northeast-2.pem bitnami@3.35.0.6
sudo apt update
sudo apt install python3-pip
pip install flask

# 다른 터미널에서 
curl localhost:5000
~~~

- SG = 보안그룹(방화벽)을 열어주지 않으면 실행되지 않음
  - manage > Networking > IPv4 Firewall > create
  - Flask 파일에서 아래와 같이 수정(누구든지 접속 가능하도록)
    ~~~python
    if __name__ == "__main__":
      app.run(host="0.0.0.0")
    ~~~
  - 다시 파일 복사 후 다시 실행
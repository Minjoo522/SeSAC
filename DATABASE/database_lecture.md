# DB

- Collection of related Information
- Stores large number of data

# DBMS System : Database Management System

- 사용자가 DB를 생성하고 관리할 수 있게 해주는 시스템
- 기본 기능 : CRUD(Create, Read, Update, Delete)

# CAP 이론

- 분산 시스템에서 일관성(Consistency), 가용성(Avaliability), 분리 내구성(Partitions Tolerance)을 모두 만족하는 것은 불가능하다
- 서비스에 맞게 적합한 DBMS를 사용

<hr>

## 동기화 : 일관성(consistance), 정확성

- 동시성 문제가 없게 : lock & busy wait 방식의 기능 구현

### Race Condition : 두 개 이상의 프로세스(쓰레드)가 동시에 공유된 자원에 접근하려고 할 때 발새하는 오류 상황

- Critical Section : 동시성이 보호 되어야 하는 구간

### 트랜잭션 : 데이터베이스의 상태를 변화시키는 하나의 작업 단위

- 하나의 트랜잭션은 Rollback되거나 commit된다
- 트랜잭션이 실패 했을 때 예외처리 -> 남은 기능 회수 : Rollback
- 성공 : commit
- 특징 : 원자성, 일관성, 독립성, 영속성

# DB 유형

## RDBMS : 관계형 데이터베이스

- MySQL, MSSQL, Sqlite3, Postgresql

## 비정형 데이터베이스

- NoSQL : 빅데이터(비정형, 규칙성 없음)
- T Value 형태

- 인스타그램, 페북 등과 같이 글, 사진, 동영상들

## Sqlite3 : 엄청 많이 사용됨

- 단일 사용자 용도로 만들어짐
- 다중 사용자(= 멀티 쓰레드) 사용시 오류가 발생할 가능성이 있음

# Table 구조

- Table
- Column
- Row
- Field
- Primary Key(기본키) : 유일한 값을 갖는 column
- Foreign Key(외래키, 참조키) : 다른 테이블을 참조할 때 사용되는 키
  - 나의 Primaty key가 상대방의 Foreign Key가 된다
- Schema(컬럼 및 속성)

<hr>

# DB용 언어 : SQL(Structured Query Language)

# 이상 현상이 발생하지 않도록 스키마를 잘 설계해야함

- 기준이 되는 ID는 절대 중복되면 안됨 : AUTOINCREMENT

## 이상 현상

- 삽입 이상 : 원치 않는 정보까지도 삽입해야 하는 현상
- 갱신 이상 : 특정 속성 값 갱신시, 중복 저장되어 있는 속성 값 중 하나만 갱신하고, 나머지는 갱신하지 않아 발생하는 데이터의 불일치 현상
- 삭제 이상 : 특정 튜플을 삭제할 경우 원하지 않는 정보까지도 삭제되는 현상

## DB 종류
- Sqlite : file DB, in-memory DB
- MySQL : DBMS 시스템 (독립적인 서버로 운영)
- PostgrSQL : 상업적인 목적으로 가장 많이 사용되는 DBMS
- MongoDB : NoSQL 기반의 DBMS 시스템
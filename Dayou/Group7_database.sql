-- Group 7 Database Design by Dayou Chen
-- For storing user data

create table Student
(
  ID        integer not null primary key autoincrement, 
  FirstName varchar(255), 
  LastName  varchar(255), 
  PassWord  varchar(255), 
  Email     varchar(255)
);

create table EnquiryInfo
(
  EnquiryID    integer(10) not null, 
  OccupationID varchar(255), 
  IndustryID   varchar(255), 
  primary key (EnquiryID), 
  foreign key(EnquiryID) references EnquiriesByStudent(EnquiryID)
);

create table Qualification
(
  ID                integer not null primary key autoincrement, 
  QualificationName varchar(255)
);

create table GovernmentData
(
  Year         integer(10), 
  IndustryID   varchar(255), 
  OccupationID varchar(255), 
  Location     varchar(255), 
  NumOfJobs    integer(10)
);

create table EnquiriesByStudent
(
  EnquiryID integer not null primary key autoincrement, 
  StudentID integer(10) not null, 
  foreign key(StudentID) references Student(ID)
);

create table Comment
(
  StudentID integer(10) not null, 
  Time      integer(10), 
  Content   varchar(255), 
  primary key (StudentID), 
  foreign key(StudentID) references Student(ID)
);

create table Occupations
(
  ID             integer not null primary key autoincrement, 
  OccupationName varchar(255)
);

create table Student_Qualification
(
  StudentID       integer(10) not null, 
  QualificationID integer(10) not null, 
  primary key (StudentID, 
  QualificationID), 
  foreign key(StudentID) references Student(ID), 
  foreign key(QualificationID) references Qualification(ID)
);

create table Occupations_Student
(
  OccupationsID integer(10) not null, 
  StudentID     integer(10) not null, 
  primary key (OccupationsID, 
  StudentID), 
  foreign key(OccupationsID) references Occupations(ID), 
  foreign key(StudentID) references Student(ID)
);

create table Images
(
  ImageID integer not null primary key autoincrement, 
  Content integer(255)
);

create table SavedImages
(
  StudentID     integer(10) not null, 
  ImagesImageID integer(10) not null, 
  primary key (StudentID, 
  ImagesImageID), 
  foreign key(StudentID) references Student(ID), 
  foreign key(ImagesImageID) references Images(ImageID)
);
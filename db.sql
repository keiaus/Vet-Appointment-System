-- Tables:
-- Pet Records
-- Pet Info
-- User Account Info
-- User Login Info
-- Vet Account Info
-- Vet Login Info
-- Admin Account Info
-- Admin Login Info
-- Appointment Info (VetID, ClientID)
-- Cancellation Info

CREATE TABLE PetInfo(
PetID INT IDENTITY(1,1) Primary Key,
PetName VARCHAR(50) NOT NULL,
PetType VARCHAR(50) NOT NULL,
PetBreed VARCHAR(50) NOT NULL,
PetColor VARCHAR(50) NOT NULL
);

CREATE TABLE UserAccountInfo(
UserID INT IDENTITY(1,1) Primary Key,
UserLoginID INT FOREIGN KEY REFERENCES UserLoginInfo(UserLoginID),
UserFirstName VARCHAR(50),
UserLastName VARCHAR(50),
UserPhoneNumber CHAR(12),
UserEmailAddress CHAR(100),
UserStreetAddress CHAR(100),
UserCity CHAR(50),
UserState CHAR(2),
UserZip    INT
);

CREATE TABLE UserLoginInfo(
UserLoginID    INT    IDENTITY(1,1) Primary Key,
UserUserName    VARCHAR(50),
UserPassword    VARCHAR(50),
);

CREATE TABLE VetAccountInfo(
VetID INT IDENTITY(1,1) Primary Key,
VetLoginID INT FOREIGN KEY REFERENCES VetLoginInfo(VetLoginID),
VetFirstName VARCHAR(50),
VetLastName VARCHAR(50),
VetPhoneNumber CHAR(12),
VetEmailAddress CHAR(100),
VetStreetAddress CHAR(100),
VetCity CHAR(50),
VetState CHAR(2),
VetZip    INT
); 

CREATE TABLE VetLoginInfo(
VetLoginID    INT    IDENTITY(1,1) Primary Key,
VetUserName    VARCHAR(50) NOT NULL,
VetPassword    VARCHAR(50) NOT NULL,
);

CREATE TABLE AppointmentInfo(
AppointmentID  INT Identity(1,1) Primary Key,
Date DATE NOT NULL,
Time TIME NOT NULL,
VetID INT FOREIGN KEY REFERENCES VetAccountInfo(VetID),
UserID INT FOREIGN KEY REFERENCES UserAccountInfo(UserID),
PetID INT FOREIGN KEY REFERENCES PetInfo(PetID),
AppointDesc    VARCHAR(500)
); 
CREATE TABLE CancellationInfo(
CancelID INT IDENTITY(1,1) Primary Key,
AppointmentID INT FOREIGN KEY REFERENCES AppointmentInfo(AppointmentID),
CancelReason VARCHAR(500) NOT NULL
); 


CREATE TABLE AdminAccountInfo(
AdminID INT IDENTITY(1,1) Primary Key,
AdminLoginID INT FOREIGN KEY REFERENCES AdminLoginInfo(AdminLoginID),
AdminFirstName VARCHAR(50),
AdminLastName VARCHAR(50),
AdminPhoneNumber CHAR(12),
AdminEmailAddress CHAR(100),
AdminStreetAddress CHAR(100),
AdminCity CHAR(50),
AdminState CHAR(2),
AdminZip    INT
);

CREATE TABLE AdminLoginInfo(
AdminLoginID    INT    IDENTITY(1,1) Primary Key,
AdminUserName    VARCHAR(50) NOT NULL,
AdminPassword    VARCHAR(50) NOT NULL,
);

CREATE TABLE PetRecords(
PetRecordID INT IDENTITY(1,1) Primary Key,
PetID INT FOREIGN KEY REFERENCES PetInfo(PetID),
PetRecordDesc VARCHAR(500) NOT NULL
);

CREATE TABLE VetScheduleInfo(
ScheduleID INT IDENTITY(1,1) Primary Key,
VetID INT FOREIGN KEY REFERENCES VetAccountInfo(VetID),
Monday VARCHAR(50),
Tuesday VARCHAR(50),
Wednesday  VARCHAR(50),
Thursday VARCHAR(50),
Friday VARCHAR(50),
Saturday VARCHAR(50),
Sunday VARCHAR(50
);
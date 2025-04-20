CREATE DATABASE Child_Therapist_Database;
USE Child_Therapist_Database;

CREATE TABLE Training_Supervisor (
    Supervisor_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Personal_Info TEXT
);

CREATE TABLE Art_Therapy_Specialist (
    Specialist_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Art_Specialization TEXT,
    Bio TEXT
);

CREATE TABLE Therapist (
    License_Number INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Age INT,
    Gender VARCHAR(10),
    Personal_Info TEXT,
    Preferred_Art_Form VARCHAR(50),
    Technique_Confidence TEXT,
    Specialization TEXT
);

CREATE TABLE Guardian (
    Guardian_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Relationship VARCHAR(50),
    Personal_Info TEXT
);

CREATE TABLE Child (
    Patient_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Preferred_Art VARCHAR(50),
    Chronic_Condition TEXT,
    Personality_Traits TEXT,
    Context_Aware_Replies TEXT,
    Personal_Info TEXT
);

CREATE TABLE Art_Therapy (
    Therapy_ID INT PRIMARY KEY,
    Art_Type VARCHAR(50),
    Medium VARCHAR(50),
    Resources TEXT,
    Benefits TEXT,
    Prompt TEXT
);

CREATE TABLE Provides_Treatment (
    License_Number INT,
    Therapy_ID INT,
    FOREIGN KEY (License_Number) REFERENCES Therapist(License_Number),
    FOREIGN KEY (Therapy_ID) REFERENCES Art_Therapy(Therapy_ID),
    PRIMARY KEY (License_Number, Therapy_ID)
);

CREATE TABLE Supports (
    Guardian_ID INT,
    Patient_ID INT,
    FOREIGN KEY (Guardian_ID) REFERENCES Guardian(Guardian_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Child(Patient_ID),
    PRIMARY KEY (Guardian_ID, Patient_ID)
);

CREATE TABLE Monitors (
    Supervisor_ID INT,
    License_Number INT,
    Start_Date DATE,
    End_Date DATE,
    Feedback TEXT,
    FOREIGN KEY (Supervisor_ID) REFERENCES Training_Supervisor(Supervisor_ID),
    FOREIGN KEY (License_Number) REFERENCES Therapist(License_Number),
    PRIMARY KEY (Supervisor_ID, License_Number)
);

CREATE TABLE Supervises (
    Specialist_ID INT,
    License_Number INT,
    Execution TEXT,
    Interpretation TEXT,
    FOREIGN KEY (Specialist_ID) REFERENCES Art_Therapy_Specialist(Specialist_ID),
    FOREIGN KEY (License_Number) REFERENCES Therapist(License_Number),
    PRIMARY KEY (Specialist_ID, License_Number)
);

CREATE TABLE Therapy_Session (
    Session_ID INT PRIMARY KEY AUTO_INCREMENT,
    Patient_ID INT,
    License_Number INT,
    Date DATE,
    Notes TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Child(Patient_ID),
    FOREIGN KEY (License_Number) REFERENCES Therapist(License_Number)
);


INSERT INTO Training_Supervisor VALUES (1, 'Dr. Morgan Hill', 'mhill@therapycenter.org', '555-9023', 'Specializes in art-based supervision.');
INSERT INTO Training_Supervisor VALUES (2, 'Dr. Amina Patel', 'apatel@mindpath.net', '555-7812', 'Focused on cognitive-behavioral guidance.');
INSERT INTO Art_Therapy_Specialist VALUES (1, 'Carlos Rivera', 'carlos@artheals.org', '555-3311', 'Clay Therapy', 'Experienced with expressive techniques.');
INSERT INTO Art_Therapy_Specialist VALUES (2, 'Linda Chen', 'lchen@expressart.org', '555-8821', 'Color Psychology', 'Paint-based therapeutic interventions.');
INSERT INTO Therapist VALUES (101, 'Alice Nguyen', 'alice@therapy.org', '555-0001', 34, 'Female', 'Works primarily with young children.', 'Sketching', 'High', 'Child Behavioral Therapy');
INSERT INTO Therapist VALUES (102, 'James Lee', 'jlee@mentalhealth.org', '555-0002', 40, 'Male', 'Focus on trauma therapy.', 'Watercolor', 'Moderate', 'Trauma-Informed Care');
INSERT INTO Guardian VALUES (1, 'Samantha Brooks', 'sbrooks@gmail.com', '555-6778', 'Mother', 'Highly involved in Liam’s care.');
INSERT INTO Guardian VALUES (2, 'Ethan Wells', 'ewells@gmail.com', '555-7890', 'Father', 'Supports Ava’s therapy remotely.');
INSERT INTO Child VALUES (1, 'Liam Brooks', 9, 'Male', 'Drawing', 'ADHD', 'Creative, Curious', 'Likes open-ended prompts', 'Sensitive information.');
INSERT INTO Child VALUES (2, 'Ava Wells', 11, 'Female', 'Painting', 'Anxiety', 'Shy, Observant', 'Prefers calm sessions', 'Sensitive information.');
INSERT INTO Art_Therapy VALUES (10, 'Mandala Coloring', 'Digital', 'Tablets, Stylus Pens', 'Improves focus and mindfulness', 'Color a mandala and reflect.');
INSERT INTO Art_Therapy VALUES (11, 'Emotion Masks', 'Paper Mache', 'Glue, Paint, Mask Forms', 'Externalize emotions safely', 'Design a mask to represent your feelings.');
INSERT INTO Provides_Treatment VALUES (101, 10);
INSERT INTO Provides_Treatment VALUES (102, 11);
INSERT INTO Supports VALUES (1, 1);
INSERT INTO Supports VALUES (2, 2);
INSERT INTO Monitors VALUES (1, 101, '2024-01-10', '2024-04-10', 'Regular feedback and solid progression.');
INSERT INTO Monitors VALUES (2, 102, '2024-02-01', '2024-05-01', 'Therapist is engaging well with clients.');
INSERT INTO Supervises VALUES (1, 101, 'Uses grounded techniques', 'Patient prefers step-by-step approach.');
INSERT INTO Supervises VALUES (2, 102, 'Highly creative strategies', 'Emphasizes visual exploration.');
INSERT INTO Therapy_Session (Patient_ID, License_Number, Date, Notes) VALUES (1, 101, '2024-03-15', 'Session focused on color exploration.');
INSERT INTO Therapy_Session (Patient_ID, License_Number, Date, Notes) VALUES (2, 102, '2024-03-20', 'Used mask-making to identify emotions.');
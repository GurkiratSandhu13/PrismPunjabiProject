## 🔊 PrismPunjabiProject: Spoofed Audio Dataset for Punjabi Language Identification (LID)

This repository contains the **dataset, code, and documentation** for a research project focused on generating acoustically diverse spoofed audio to test the robustness of **Language Identification (LID)** models for the Punjabi language.

---

### 1. Project Goal

The primary goal is to create a challenging, **high-quality, and highly diverse acoustic dataset** that simulates **real-world playback attacks**, specifically targeting the **Punjabi language** (using original source clips from **AI4BHARAT**). The dataset incorporates extensive variability in:

* **Speaker demographics**
* **Dialects** (Majhi, Malwai, Puadhi)
* **Recording distances**
* **Acoustic environments**

---

### 2. Repository Structure

The project is logically divided into four main directories:


PrismPunjabiProject/
├── LICENSE.md                  <- Custom license requiring attribution and contact.
├── README.md                   <- This file.
├── Literature Review/          <- Academic background and methodology.
│   └── Literature_Review.md
├── Novel Dataset/              <- Contains the complete dataset (audio files are structured into sub-folders).
│   ├── Bonafide/               <- Clean, original source clips (Reference Audio), organized by speaker.
│   │   ├── female 1 audio/
│   │   ├── female 2 audio/
│   │   ├── female 3 audio/
│   │   ├── female 4 audio/
│   │   ├── male 1 audio/
│   │   ├── male 2 audio/
│   │   └── male 3 audio/
│   ├── Spoofed/                <- Degraded audio segments, organized by speaker and recording attempt.
│   │   ├── f1 spoofed 1/       <- Female 1, Attempt 1
│   │   ├── f1 spoofed 2/       <- Female 1, Attempt 2
│   │   ├── f2 spoofed 1/       <- Female 2, Attempt 1
│   │   ├── f2 spoofed 2/       <- Female 2, Attempt 2
│   │   ├── f3 spoofed 1/       <- Female 3, Attempt 1
│   │   ├── f3 spoofed 2/       <- Female 3, Attempt 2
│   │   ├── f4 spoofed 1/       <- Female 4, Attempt 1
│   │   ├── f4 spoofed 2/       <- Female 4, Attempt 2
│   │   ├── m1 spoofed 1/       <- Male 1, Attempt 1
│   │   ├── m1 spoofed 2/       <- Male 1, Attempt 2
│   │   ├── m2 spoofed 1/       <- Male 2, Attempt 1
│   │   ├── m2 spoofed 2/       <- Male 2, Attempt 2
│   │   ├── m3 spoofed 1/       <- Male 3, Attempt 1
│   │   └── m3 spoofed 2/       <- Male 3, Attempt 2
│   ├── wav audios/             <- Raw, unsegmented audio recordings from the initial sessions.
│   └── master_metadata.csv     <- Comprehensive metadata (2,000+ records) linking to all files.
│
├── Python Codes/               <- Scripts for data processing and quality analysis.
│   ├── batch_segmentation.py   <- Script for splitting long audio into utterances.
│   ├── quality_metrics.py      <- Script to calculate SNR and PESQ scores.
│   └── utilities/              <- Helper functions and custom libraries.
│
└── Reports/                    <- Progress reports and quality validation results.
    ├── Progress_Report_V1.md   <- Comprehensive project report.
    └── PESQ_SNR_Analysis.pdf   <- Full quality indicator report.


### 3. Team and Contributions

The project was executed through collaborative effort with clear roles for data generation, quality assurance, and processing.

| Team Member | Role | Contribution |
| :--- | :--- | :--- |
| **Gurkirat Singh** (23BAI70476) | **Data Lead** | Data Set Generation (Recording sessions), Initial Processing, Segment Batching, Final Data Structuring. |
| **Ashmit Singh** (23BAI70335) | **Metadata Specialist** | Designing and Maintaining the `master_metadata.csv` sheet, ensuring consistency of all data labels. |
| **Harsh Jain** (23BAI70194) | **Quality Analyst** | Developing and running Python scripts for Quality Indicators (SNR, PESQ) and handling general script execution. |
| **Charanjit Singh** (23BAI70124) | **Data Contributor** | Participation in controlled recording sessions. |
| **GUNPREET SINGH** (23BAI71443) | **Data Contributor** | Participation in controlled recording sessions. |
| **BHUMI KAPOOR** (23BAI70524) | **Data Contributor** | Participation in controlled recording sessions. |
| **External Contributors** | **Speakers** | Various students (including parents and students from other universities) providing diverse demographic and dialectal coverage. |

---

### 4. Dataset Generation Details

#### 4.1. Speaker and Dialect Diversity

The dataset was collected from **over 6 speakers** over **30 days** in controlled and natural environments. Speakers included family members (mother, sister, male cousin) and students from various institutions, ensuring a wide range of age groups, genders, and regional accents.

**Dialectal Coverage:**

* **Majhi:** Considered the **standard dialect**.
* **Malwai:** Widely spoken dialect, known for distinct vowel and tonal shifts.
* **Puadhi:** Spoken in the South-Eastern regions of Punjab, providing unique phonological features.

#### 4.2. Metadata Field Definitions (Example from `master_metadata.csv`)

The dataset features granular metadata to track acoustic conditions. The final file structure uses a hierarchy that maps precisely to these labels (e.g., `Spoofed_Data/1.0m_Records/`).

| Field | Purpose |
| :--- | :--- |
| `recording_id` | Unique ID for the recording session. |
| `speaker_id` | Anonymized unique ID for the speaker. |
| `sentence_id` | ID of the source text used (from AI4BHARAT). |
| `transcript` | The exact sentence text. |
| `language_tag` | Specifies the **dialect**: PUN-Majhi, PUN-Malwai, PUN-Puadhi. |
| `gender` | Speaker gender. |
| `recording_device_model` | The device used to capture the spoofed audio (e.g., specific phone model). |
| `playback_device` | The device playing the source audio (e.g., specific speaker model). |
| `distance_from_source` | Measured **distance**: 0.5m, 1m, 2m. |
| `azimuth_angle` | Horizontal **angle** of the recorder relative to the speaker (e.g., 0°, 45°). |
| `direction` | General **direction**: On-axis, Off-axis (Left). |
| `room_noise` | Description of **ambient noise level** (e.g., Quiet (Conference Room), Residential Noise). |
| `replay_count` | Instance number if the segment was repeated. |
| `spoofed_or_bonafide` | Data **category**: Spoofed or Bonafide. |
| `audio_file` | Final processed file name. |
| `file_format` | WAV file specifications (**16kHz, 16-bit**). |
| **PESQ Score** | Objective measure of **perceptual speech quality** (1.0-4.5). |
| **SNR (dB)** | **Signal-to-Noise Ratio** (acoustic quality). |

---

### 5. License and Usage Policy

This project is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)**.

> **Note on GitHub Licensing:** GitHub's default license picker focuses on common software licenses. Since this project primarily distributes a dataset and documentation, the **CC BY-NC-ND 4.0 license** is legally appropriate for these assets and aligns with the need for high restriction and mandatory attribution. We have included the full license text in the `LICENSE.md` file, which is the necessary step for licensing on GitHub.

This license is the most restrictive Creative Commons license and ensures:

* **Attribution (BY):** You must credit the original creators (the team listed above).
* **NonCommercial (NC):** The work cannot be used for commercial purposes.
* **NoDerivatives (ND):** If you share the material, you must do so in its unmodified form.

Crucially, **to use the dataset for ANY purpose** (including academic research), you must first consult with the Project Lead, **Gurkirat Singh**, as detailed in the LICENSE file.
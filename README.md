# RAUS
# Software Requirements Specification (SRS)

## سامانه هوشمند دیکته و گزارش‌دهی سونوگرافی

---

## 1. مقدمه

### 1.1 هدف سند

این سند با هدف تعریف کامل نیازمندی‌های نرم‌افزاری سامانه «دیکته و گزارش‌دهی هوشمند سونوگرافی» تهیه شده است. این سامانه به منظور کمک به پزشکان و سونوگرافیست‌ها برای تولید سریع، دقیق و ساختارمند گزارش‌های سونوگرافی با استفاده از گفتار طراحی می‌شود.

### 1.2 دامنه سیستم

سیستم یک نرم‌افزار تجاری پزشکی است که گفتار پزشک را دریافت کرده، به متن تبدیل می‌کند، مفاهیم پزشکی سونوگرافی را استخراج نموده و گزارش استاندارد سونوگرافی تولید می‌نماید.

### 1.3 کاربران هدف

* پزشکان رادیولوژیست
* سونوگرافیست‌ها
* مراکز تصویربرداری و کلینیک‌ها
* مدیر سیستم مرکز درمانی

---

## 2. توصیف کلی سیستم

### 2.1 دیدگاه محصول

این سامانه می‌تواند به صورت:

* نرم‌افزار دسکتاپ (ویندوز)
* یا وب‌اپلیکیشن مبتنی بر سرور داخلی مرکز
  پیاده‌سازی شود.

### 2.2 قابلیت‌های سطح بالا

* ضبط گفتار پزشک
* تبدیل گفتار به متن فارسی پزشکی
* تشخیص اصطلاحات تخصصی سونوگرافی
* تولید گزارش ساختارمند
* خروجی PDF و Word

---

## 3. Epics

* Epic 1: User Management & Authentication
* Epic 2: Speech Recording & STT Processing
* Epic 3: Medical NLP & Report Generation
* Epic 4: Reporting Templates & Editing
* Epic 5: Data Storage & Security
* Epic 6: Kafka & InfluxDB Integration
* Epic 7: Data Validation & Processing Pipeline
* Epic 8: ML Model Training & MLOps
* Epic 9: Monitoring & Testing
* Epic 10: Deployment & CI/CD Pipeline

---

## 4. Acceptance Criteria

* AC1: Latency تبدیل گفتار به متن < 2 ثانیه
* AC2: دقت تبدیل گفتار به متن حداقل ۹۰٪ در محیط واقعی
* AC3: گزارش تولید شده کاملاً قابل استفاده و مطابق قالب استاندارد باشد
* AC4: دسترسی کاربر محدود به داده‌های خودش باشد
* AC5: تمامی سرویس‌ها به صورت containerized و مستقر در Kubernetes cluster باشند
* AC6: Kafka messages با Schema Registry هماهنگ و بدون خطا منتقل شوند
* AC7: داده‌های high-frequency time-series در InfluxDB به درستی ذخیره شوند
* AC8: تست‌های Unit، Integration و Performance با موفقیت پاس شوند
* AC9: Monitoring metrics در Prometheus/Grafana نمایش داده شوند
* AC10: داده‌ها به صورت امن در PostgreSQL، MongoDB و S3 ذخیره شوند و دسترسی‌ها طبق IAM کنترل شوند

---

## 5. نیازمندی‌های عملکردی (Functional Requirements)

### 5.1 مدیریت کاربر

* FR-01: سیستم باید امکان تعریف کاربران با نقش‌های مختلف (پزشک، ادمین) را داشته باشد.
* FR-02: هر کاربر باید فقط به گزارش‌های خود دسترسی داشته باشد.

### 5.2 ضبط و پردازش صدا

* FR-03: سیستم باید امکان ضبط زنده صدا از میکروفون را فراهم کند.
* FR-04: سیستم باید گفتار فارسی پزشکی را به متن تبدیل کند.
* FR-05: سیستم باید امکان توقف، ادامه و حذف ضبط را داشته باشد.

### 5.3 پردازش زبان پزشکی سونوگرافی

* FR-06: سیستم باید اصطلاحات آناتومیک (کبد، کلیه، رحم، تخمدان و …) را تشخیص دهد.
* FR-07: سیستم باید اندازه‌ها (میلی‌متر، سانتی‌متر) را استخراج کند.
* FR-08: سیستم باید وضعیت طبیعی/غیرطبیعی را تشخیص دهد.

### 5.4 گزارش‌دهی ساختارمند

* FR-09: سیستم باید گزارش را در قالب بخش‌های استاندارد تولید کند:

  * Indication
  * Technique
  * Findings
  * Impression
* FR-10: سیستم باید قالب‌های مختلف سونوگرافی را پشتیبانی کند:

  * سونوگرافی شکم و لگن
  * سونوگرافی بارداری
  * سونوگرافی تیروئید

### 5.5 ویرایش و تأیید گزارش

* FR-11: کاربر باید بتواند متن گزارش را ویرایش کند.
* FR-12: سیستم باید تغییرات کاربر را ذخیره کند.

### 5.6 خروجی و ذخیره‌سازی

* FR-13: سیستم باید خروجی PDF تولید کند.
* FR-14: سیستم باید خروجی Word تولید کند.
* FR-15: سیستم باید گزارش‌ها را آرشیو کند.

---

## 6. Tasks و Issue مرحله به مرحله (Jira/Trello-ready)

### Sprint 1 – Setup پایه و DevOps

| Task    | Description                                      | Est. Time | Priority | Epic    |
| ------- | ------------------------------------------------ | --------- | -------- | ------- |
| T1.1    | راه‌اندازی پروژه Electron + React                | 1 روز     | High     | Epic 1  |
| T1.2    | ایجاد Repo Git و Branching Strategy              | 0.5 روز   | High     | Epic 10 |
| T1.3    | پیاده‌سازی Dockerfile برای سرویس‌ها              | 1 روز     | High     | Epic 10 |
| T1.4    | استقرار نمونه microservice در Kubernetes Cluster | 2 روز     | High     | Epic 10 |
| T1.5    | راه‌اندازی GitHub Actions CI/CD                  | 1 روز     | High     | Epic 10 |
| Issue 1 | Failure در deploy microservice اولیه             | -         | Critical | Epic 10 |

### Sprint 2 – Kafka & InfluxDB Integration

| Task    | Description                                   | Est. Time | Priority | Epic   |
| ------- | --------------------------------------------- | --------- | -------- | ------ |
| T2.1    | استقرار resilient Kafka cluster با Strimzi    | 2 روز     | High     | Epic 6 |
| T2.2    | فعال‌سازی Schema Registry برای Kafka          | 1 روز     | High     | Epic 6 |
| T2.3    | استقرار InfluxDB برای داده‌های high-frequency | 1 روز     | High     | Epic 6 |
| T2.4    | اتصال سرویس‌ها به Kafka و InfluxDB            | 2 روز     | High     | Epic 6 |
| Issue 2 | پیام‌ها از Kafka نرسد یا Schema mismatch      | -         | Critical | Epic 6 |

### Sprint 3 – Data Storage & Security

| Task    | Description                                    | Est. Time | Priority | Epic   |
| ------- | ---------------------------------------------- | --------- | -------- | ------ |
| T3.1    | Provision PostgreSQL برای داده‌های ساختاریافته | 1 روز     | High     | Epic 5 |
| T3.2    | Provision MongoDB برای لاگ‌ها و anomalyها      | 1 روز     | High     | Epic 5 |
| T3.3    | ایجاد S3 bucket برای raw data lake             | 0.5 روز   | High     | Epic 5 |
| T3.4    | تنظیم IAM roles / policies برای سرویس‌ها       | 1 روز     | High     | Epic 5 |
| T3.5    | ذخیره connection strings در Kubernetes Secrets | 0.5 روز   | High     | Epic 5 |
| Issue 3 | دسترسی سرویس‌ها به storage محدود یا خطا        | -         | Critical | Epic 5 |

### Sprint 4 – Data Processing & Validation

| Task    | Description                                      | Est. Time | Priority | Epic   |
| ------- | ------------------------------------------------ | --------- | -------- | ------ |
| T4.1    | Build Flink validation service                   | 2 روز     | High     | Epic 7 |
| T4.2    | پیاده‌سازی model-based reconciliation algorithms | 3 روز     | High     | Epic 7 |
| T4.3    | پیاده‌سازی real-time validation rules engine     | 3 روز     | High     | Epic 7 |
| T4.4    | Data routing logic برای classification           | 2 روز     | High     | Epic 7 |
| Issue 4 | Invalid data not flagged correctly               | -         | Critical | Epic 7 |

### Sprint 5 – Data Transformation & ML Pipeline

| Task    | Description                                                        | Est. Time | Priority | Epic   |
| ------- | ------------------------------------------------------------------ | --------- | -------- | ------ |
| T5.1    | آماده‌سازی و transform داده‌های clean برای ML                      | 3 روز     | High     | Epic 8 |
| T5.2    | ایجاد pipeline برای feature selection, extraction & transformation | 3 روز     | High     | Epic 8 |
| T5.3    | اعمال اصول MLOps و مدیریت چرخه عمر مدل‌ها                          | 2 روز     | High     | Epic 8 |
| Issue 5 | Feature pipeline خطا یا داده ناقص                                  | -         | High     | Epic 8 |

### Sprint 6 – Monitoring & Testing

| Task    | Description                                            | Est. Time | Priority | Epic   |
| ------- | ------------------------------------------------------ | --------- | -------- | ------ |
| T6.1    | Prometheus/Grafana برای متریک‌ها و مانیتورینگ          | 2 روز     | High     | Epic 9 |
| T6.2    | نوشتن تست‌های Unit, Integration, Performance با Pytest | 3 روز     | High     | Epic 9 |
| T6.3    | بهینه‌سازی سرویس‌ها و رفع bottleneckها                 | 2 روز     | High     | Epic 9 |
| Issue 6 | Metrics نمایش داده نشود یا تست‌ها fail شوند            | -         | Critical | Epic 9 |


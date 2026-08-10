# Marizabel Camargo
**Software Engineer**

Sault Ste. Marie, ON, Canada | marizabelcmg@gmail.com | (705) 975-8871 | Canadian Citizen
linkedin.com/in/marizabel-camargo | github.com/marizabel

## Professional Summary

Software Engineer with 13+ years of experience, primarily in Java backend development with real depth in enterprise integration (APIs, ESBs, B2B) and cloud infrastructure. Built systems end to end, including an identity resolution platform built from scratch (backend, frontend, database, security, deployment). Worked specifically on identity and access: SSO/JWT, role-based access control, and zero-trust architecture on Kubernetes. Uses Claude Code and other AI tools daily. Prefers owning things end to end rather than just a slice of a ticket.

## Skills

- **Languages:** Java, Kotlin, SQL, JavaScript, Groovy
- **Frontend:** React, HTML, CSS, JavaScript, jQuery, Bootstrap, Ajax
- **Design:** Figma (basic prototyping/wireframes)
- **Backend & Data Access:** Spring Boot, Spring Data JPA, Hibernate (incl. caching), JSP, Struts, Transaction Management, Spring Security, Concurrency, Distributed Systems, Microservices, Design Patterns (Factory, Strategy, Singleton), Stored Procedures
- **Resilience & Async Patterns:** Exponential backoff retry, circuit breaker, webhook consumers, caching, heartbeat health checks
- **Identity & Access Management:** SSO, JWT, OAuth, role-based access control design (authorization/profile/permission tables), digital certificate authentication, Zero Trust architecture (Istio AuthorizationPolicies), Azure Workload Identity, Azure Entra ID, Azure Key Vault
- **Databases:** SQL Server, Oracle, DB2, Sybase, MySQL
- **Data & ETL:** SSIS (package-based and project deployment models), SQL Server data processing pipelines
- **Job Orchestration & Scheduling:** ActiveBatch, Cron Jobs (job orchestration, file transfer automation, critical task scheduling)
- **CI/CD & Code Quality:** GitHub Actions, TeamCity, Octopus Deploy, Jenkins, Git, GitOps, GitLab, Maven, Gradle, Snyk (static analysis), SonarQube, JUnit, Mockito, Selenium, BDD
- **AI & Developer Tooling:** GitHub Copilot, Claude Code, Microsoft Copilot, MCP servers, LLM-assisted development & code review
- **Cloud & Infrastructure:** Azure, Azure Kubernetes Service (AKS), Docker, Kubernetes, Istio Service Mesh, mTLS, Zero Trust, Azure Key Vault (secrets management), Application Gateway (AGC), Application Load Balancer (ALB), F5
- **Integration & Messaging:** Software AG webMethods (Integration Server, Designer/Developer, My webMethods Server, Trading Networks, Universal Messaging/Broker), REST APIs, SOAP, API Gateways, JMS, MQ, XML, JSON, B2B/EDI
- **Security:** TLS/SSL, HTTPS, PGP Encryption, Digital Certificates, Public/Private Key Cryptography
- **Observability:** Dynatrace (ESB traffic monitoring), application/job log analysis and alerting
- **Accessibility:** WCAG 2.0, W3C accessibility standards, assistive technology support (JAWS, NVDA)
- **Tools & Operations:** ServiceNow (incident/change management), Linux administration & scripting
- **Methodologies:** Agile/Scrum, Kanban, SAFe, Scrum Master

## Certifications

- Microsoft Certified: Azure Fundamentals (AZ-900)
- Certified ScrumMaster (CSM)

## Experience

### Senior Software Engineer | Ontario Lottery and Gaming (OLG)
**Aug 2024 – Present | Sault Ste. Marie, ON | Hybrid**

Owns OLG's identity resolution and AML compliance platforms end to end, from architecture through production support.

- Designed and built Provincial Player ID (PPID) from scratch — OLG's first in-house identity resolution platform. Merges player profiles from multiple gaming providers into one identity record for compliance, fraud, and investigation teams. Built the backend in Java 21/Spring Boot (using Virtual Threads), the frontend in React/Vite, the database in SQL Server, wrote the Dockerfiles, and deployed it to Azure Kubernetes Service (AKS).
- Led the decision to build PPID in-house instead of buying a vendor solution, then owned the architecture and delivery, avoiding recurring vendor licensing costs.
- Designed the matching engine that decides if two profiles are the same person: exact and fuzzy string comparison, weighted scoring, and a configurable confidence threshold. Matches above the threshold resolve automatically; everything else routes to a human reviewer with full source-profile traceability. PPID manages 1–2M+ profiles and resolves ~30,000 new ones per day.
- Added exponential backoff retry and a circuit breaker around PPID's webhook and database calls (both async and can fail independently).
- Built a webhook listener triggered by another microservice when its matching run finishes, which kicks off PPID's processing of the resulting primary profiles.
- Added caching for already-resolved enterprise profiles, configuration settings, and daily upsert batches to reduce repeated database hits.
- Used parameterized stored procedures to send data in batches instead of loading everything into memory at once, preventing JVM heap issues on large volumes.
- Set up SSO login via Azure Entra ID, with JWT tokens authenticating the frontend to the backend.
- Established CI/CD from nothing for a team that used to deploy by hand. Cut deploy time from ~4 hours to ~20 minutes; added Snyk static analysis and automated test gates.
- Migrated a Java microservices platform from on-premises to AKS. Set up Istio service mesh for automatic mTLS, added Istio AuthorizationPolicies so services can only call what they're explicitly allowed to call, used Azure Workload Identity so pods authenticate without stored credentials, and a Key Vault CSI driver to deliver certificates at runtime. Also built a JKS truststore via an init container at pod startup. Everything (namespaces, Istio policies, gateways, CronJobs, PodDisruptionBudgets) is defined as code and deployed through Octopus pipelines.
- Modernized SSIS package delivery: moved from manual .dtsx files to a project-based model with Git, automated TeamCity builds, versioned .ispac artifacts, and Octopus Deploy pipelines. Cut deployment cycle time by ~78% and removed the team's dependency on a DBA for routine deploys.
- Took over ownership of ActiveBatch job orchestration (scheduling file transfers and backend tasks), learned it independently, and brought it in-house.
- Proposed and ran a phased staged deployment for a new iGaming data integration into RTMS to catch bad deploys early — nobody asked for it; chosen because unwinding a bad production deploy on this integration would have been expensive.
- Uses Claude Code, GitHub Copilot, and MCP-based agents daily for coding, debugging, and design work. Reviews every change before it reaches production.
- On the on-call rotation; owns root cause analysis when incidents occur and documents them to prevent recurrence.
- Tech lead on Patron Risk Scoring/Rating, a second in-house platform integrating with PPID: mentors developers, owns architecture, DevOps, CI/CD, cloud infrastructure, cloud security, and runs code reviews.
- Mentors junior and mid-level engineers (including a student) through code reviews and architecture discussions; interviews engineering candidates.
- Runs cross-team knowledge-transfer sessions on CI/CD, Git/GitHub, and SSIS changes. Trained the QA team to run ActiveBatch jobs and expand database-level test coverage.
- Leads standups when the PM is out and runs demos for the business.

### Software Integration Engineer | Ontario Lottery and Gaming (OLG)
**May 2022 – Aug 2024 | Sault Ste. Marie, ON | Hybrid**

Primary hands-on developer for OLG's integration layer, connecting internal systems and external vendors through a Software AG webMethods ESB.

- Built and supported 10+ B2B integrations end to end (requirements through production support) using webMethods Integration Server, Designer/Developer, and My webMethods Server (MWS).
- Secured integrations carrying player PII, banking info, and transaction data using TLS/SSL, PGP encryption, and digital certificates.
- Built ETL/SSIS pipelines that fed player transaction data into regulatory systems, including FinTRAC reporting.
- Set up and ran ActiveBatch job orchestration to schedule and manage file transfers and backend tasks for AML processing.
- Configured and troubleshot Universal Messaging/Broker and JMS/MQ, using heartbeat health checks to detect endpoint failures.
- Used Dynatrace to monitor ESB traffic and troubleshoot performance, plus manual log analysis for ActiveBatch jobs, SSIS runs, and Java application logs.
- Deployed on-premises by logging directly into Linux servers to run deployments, investigate errors, and handle production support.
- Built Java/Kotlin backend services alongside webMethods work, and supported DevOps pipelines (GitLab, TeamCity, Octopus Deploy) and Kubernetes/Docker infrastructure.
- Handled incident and change management through ServiceNow; performed Linux administration/scripting to keep integration infrastructure stable.

### Full Stack Software Developer | Softplan Planejamento e Sistemas
**Jan 2013 – Aug 2021 (8 yrs 8 mos, incl. internship & promotion) | Florianopolis, Brazil**

Full stack developer on one of Brazil's highest-traffic judicial platforms, used daily by millions of lawyers and judges, built on Java, Spring, and Hibernate.

- Built the platform's digital case file viewer: displayed legal process documents as PDFs with auto-advancing pagination, multi-document selection, and PDF-to-HTML/JavaScript/jQuery rendering (to bypass browser plugin inconsistencies).
- Fixed bugs, added features, and maintained the platform's role-based access control system: authorization tables linked user profiles (e.g. 'attorney') to permission sets, with users able to hold multiple profiles.
- Supported login via physical digital certificate on a USB token (read through a Java browser plugin) in addition to standard username/password.
- Built an opt-in beta program ('canario'): users could join a capped list (~100 out of ~500K total) and revert to the previous version through a portal link.
- Eliminated duplicated business logic spread across multiple applications by building a shared microservice. Applied Factory, Strategy, and Singleton design patterns. Improved overall system quality by 31% and removed a recurring source of bugs.
- Optimized backend performance: rewrote slow SQL queries, cleaned up JDBC connection handling, and applied Hibernate caching where appropriate.
- Made the platform accessible for users with visual disabilities: WCAG 2.0 and W3C standards, tested with JAWS and NVDA screen readers.
- Built an automated test suite (JUnit, Mockito, Selenium, BDD, Groovy) that cut system defects by 22%.
- Set up CI/CD pipelines (Git, GitLab, Jenkins, SonarQube, Maven, Gradle) and led code reviews.
- Built features on older parts of the platform using JSP, Struts, PHP, and AngularJS (circa 2017–2018).
- Took ownership of planning and delivery for a major project as both developer and Scrum Master: cleared blockers, aligned the team with business goals, and delivered on schedule.

## Education

**Postgraduate Certificate — IT Project Management**
Instituto Brasileiro de Formação (IBF Pós) | 2020–2021 | Brazil

**Advanced Diploma — Systems Analysis and Development (3-Year Program)**
SENAI/SC | 2012–2015 | Florianópolis, Brazil
Credential-evaluated (ECA) as equivalent to a Canadian 3-year college diploma in Information Technology.

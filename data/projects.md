# Projects

## Provincial Player ID (PPID) — Identity Resolution Platform
- **Description:** Enterprise identity resolution platform that consolidates player profiles from multiple gaming providers into a single Enterprise Identity, supporting AML investigations, compliance, fraud detection, and regulatory reporting. Manages ~1–2M profiles and processes ~30,000 new profiles daily, with horizontal scaling via AKS.
- **Highlights:** Configurable matching engine using exact and fuzzy comparisons, weighted scoring, and configurable thresholds. Supports automatic matching, human review of ambiguous cases, source-profile traceability, and primary-profile selection based on completeness and recency.
- **Technologies:** Java 21, Spring Boot, Virtual Threads, React, Vite, SQL Server, SSIS, Docker, Kubernetes, Azure AKS, Istio, mTLS, SSO, JWT, Snyk, Azure Monitor, CI/CD, Claude CLI
- **My role:** Designed and built the platform end to end — architecture, Java/Spring Boot backend, React frontend, SQL Server database design, SSIS integration, security, automated testing, CI/CD, and deployment to AKS.
- **Associated with:** Ontario Lottery and Gaming (OLG) | Nov 2025 – July 2026

## Cloud Migration: On-Premises to Azure AKS
- **Description:** Migrated a Java microservices platform from on-premises infrastructure to Azure Kubernetes Service (AKS), replacing an F5 hardware load balancer with Azure Application Gateway for Containers (AGC) and Istio service mesh for automatic mTLS between services.
- **Highlights:** Zero-trust security with Istio AuthorizationPolicies, Azure Workload Identity for credential-free pod authentication, Key Vault CSI driver for runtime certificate delivery, and SQL Server TLS validation using a JKS truststore built by an init container. All cluster resources defined as code and deployed through automated Octopus pipelines.
- **Technologies:** Azure AKS, Istio, Azure Key Vault, AGC, Workload Identity, Spring Boot, Octopus Deploy, Kubernetes Gateway API
- **My role:** Owned the full migration — security architecture, Istio setup, identity/secrets configuration, and infrastructure-as-code for all cluster resources.
- **Associated with:** Ontario Lottery and Gaming (OLG) | Jun 2026 – Aug 2026

## SSIS CI/CD Modernization
- **Description:** Designed and implemented end-to-end modernization of a legacy SSIS delivery process, migrating from manually managed .dtsx packages to a project-based model with version control and automated CI/CD.
- **Highlights:** Reduced deployment cycle time by ~78%, removed routine DBA dependency, improved rollback and auditing, eliminated hardcoded environment configuration, and centralized logging and execution history in SSISDB.
- **Technologies:** SSIS, SQL Server, SSIS Catalog, SSISDB, GitHub, TeamCity, Octopus Deploy, ActiveBatch
- **My role:** Designed and implemented the full solution — Git-based workflow, automated TeamCity builds, versioned .ispac artifacts, and Octopus Deploy pipelines for dev/staging/production promotion.
- **Associated with:** Ontario Lottery and Gaming (OLG) | Aug 2025 – Nov 2025

## Portfolio Assistant
- **Description:** AI assistant that answers questions about my professional experience using RAG (Retrieval-Augmented Generation). Recruiters can chat with it and ask about my skills, experience, and projects instead of reading a static resume.
- **Technologies:** Python, LangChain, Gemini Flash (Google AI), sentence-transformers, ChromaDB, Streamlit
- **My role:** Built the entire project — RAG pipeline, vector store setup, Streamlit chat interface, CI/CD-ready structure, and deployment planning for Hugging Face Spaces.
- **Link:** github.com/marizabel/portfolio-assistant

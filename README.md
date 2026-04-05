# 🎬 Cinema Manager

A terminal-based cinema management system built in Python, featuring role-based access for **Administrators** and **Customers**. Developed as a university project at the University of Brasília (UnB).


## Overview

Cinema Virtual simulates the core workflow of a cinema — managing films, sessions, tickets, and a snack bar entirely through a terminal interface. The system demonstrates object-oriented programming principles with a clean package-based architecture and JSON file persistence.


## Features

### Two User Roles

**Administrator**
- Add and manage films (title, genre, duration).
- Create screening sessions (film, time slot).
- Add products to the snack bar.

**Customer**
- Browse available films and sessions.
- Purchase tickets for any session.
- Buy snacks from the snack bar.
- View personal ticket history.

All data is stored in JSON files under `packages/db/`:
- `administrador.json` Admin credentials.
- `sessao.json` Screening sessions.
- `cliente.json` Customer accounts and purchased tickets.
- `lanche.json` Snack bar inventory.


## 🛠️ Tech Stack


- **Language:** Python 3.x.
- **Architecture:** Object-Oriented Programming (OOP).
- **Storage:** JSON file persistence.
- **Interface:** Terminal (CLI).


## 🚀 Getting Started

### Prerequisites
- Python 3.x installed.

### Run the application
```bash
git clone https://github.com/RodrigoDutraF88/CINEMA-RODRIGO-DUTRA-FERREIRA.git
cd CINEMA-RODRIGO-DUTRA-FERREIRA
python main.py
```


## Default Admin Credentials
```
Name:          Rodrigo
CPF:           1234
Password:      4321
```

## 📂 Project Structure

```
CINEMA-RODRIGO-DUTRA-FERREIRA/
├── main.py              # Entry point
├── testbench.py         # Test cases
├── .gitignore
└── packages/
    └── db/              # JSON data files
        ├── administrador.json
        ├── sessao.json
        ├── cliente.json
        └── lanche.json
```

**University:** University of Brasília (UnB)  
**Author:** Rodrigo Dutra Ferreira

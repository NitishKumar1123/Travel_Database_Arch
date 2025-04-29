### Travel Itinerary Management Backend
<!-- ```markdown -->
This is a backend system for managing travel itineraries, developed as part of a full-stack SDE intern assignment. The system includes a database architecture for trip itineraries, RESTful API endpoints for managing itineraries, and an MCP server for recommending itineraries based on the number of nights.

### Features

- **Database Schema:** Design and implementation of a database schema to manage trip itineraries, including hotel accommodations, transfers, and activities.
- **API Endpoints:**
  - **Create Itinerary:** Allows creating new travel itineraries.
  - **View Itinerary:** Allows viewing existing itineraries.
- **MCP Server:** A server that provides recommended itineraries based on the number of nights.

### Tech Stack

- **Python 3.12+**
- **FastAPI** for creating RESTful APIs
- **SQLAlchemy** for database ORM
- **Uvicorn** for running the FastAPI application
- **pytest** for testing the API endpoints

### Getting Started

### Prerequisites

- Python 3.12+ installed on your machine.
- Virtual environment (optional but recommended).

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/NitishKumar1123/Travel_Database_Arch.git
   cd Travel_Database_Arch
   ```

2. Create and activate a virtual environment:

   - **Windows:**

     ```bash
     python -m venv venv
     ./venv/Scripts/activate
     ```

   - **Linux/macOS:**

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   You can manually seed the database using the following command:

   ```bash
   python -m app.seed
   ```

### Running the Application

To start the server:

```bash
uvicorn app.main:app --reload
```

The server will run at `http://127.0.0.1:8000`.

### API Endpoints

1. **Create Itinerary**
   - **POST /itineraries**
   - Request body: JSON with trip itinerary details (name, days, accommodations, transfers, activities).

2. **View Itinerary**
   - **GET /itineraries/{id}**
   - Returns the details of a specific itinerary by ID.

### Running Tests

To run the test suite:

```bash
python -m pytest tests/
```

All tests should pass without issues.

## Project Structure

```
Travel_Database_Arch/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app and routing
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic models for request/response validation
│   ├── database.py      # Database connection and session management
│   ├── seed.py          # Script to seed the database with data
│   └── mcp.py           # MCP server logic for itinerary recommendations
├── tests/
│   ├── test_endpoints.py    # API endpoint tests
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Contributing

Feel free to fork the repository and submit pull requests for improvements. Make sure to add tests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
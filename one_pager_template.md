# Travel Database Architecture - One-Pager Documentation

## Steps Followed to Complete the Assignment

1. **Project Setup**
   - Initialized a new project directory and created a virtual environment for dependency management.
   - Installed necessary Python packages: FastAPI, SQLAlchemy, Pydantic, etc.
   - Set up the directory structure with separate folders for models, routes, database configurations, and schemas.

2. **Database Architecture Design**
   - Designed the database schema for travel itineraries using SQLAlchemy.
   - Created models for `HotelStay`, `Transfer`, `Activity`, `ItineraryDay`, and `Itinerary`.
   - Implemented relationships between these models, ensuring that day-wise itineraries and other components like transfers, activities, and accommodations were properly linked.
   - Seeded the database with sample data for the Phuket and Krabi regions in Thailand.

3. **API Development**
   - Developed RESTful API endpoints for creating and viewing itineraries.
   - Used FastAPI to create the necessary routes for:
     - Creating a new trip itinerary (`POST /itineraries`).
     - Viewing existing itineraries (`GET /itineraries`).
   - Ensured input validation, error handling, and response formatting were implemented using Pydantic models.

4. **MCP Server Implementation**
   - Created a simple server to recommend itineraries based on the number of nights.
   - Integrated the itinerary logic with the MCP server to return recommended trips for various durations (2-8 nights).

5. **Testing**
   - Created unit tests for the API endpoints and database interactions.
   - Used `pytest` to ensure the correctness of API endpoints and database seeding.
   - Validated that all tests passed successfully.

6. **Documentation**
   - Wrote detailed `README.md` documentation for the project, covering installation instructions, API usage, and expected responses.

## Key Decisions Made During Implementation

- **Database Schema Design:**
  - Chose a relational database model to represent the relationships between hotels, transfers, activities, and itineraries.
  - Used SQLAlchemy’s ORM features to define the relationships (One-to-Many, Many-to-One).

- **API Framework:**
  - Opted for FastAPI due to its simplicity and performance for building APIs. It provides automatic validation and interactive API documentation through Swagger UI.

- **Seeding Data:**
  - Decided to seed data specifically for the Phuket and Krabi regions to simulate realistic trip itineraries for testing and demonstrations.

- **MCP Server:**
  - Used a basic algorithm to recommend itineraries based on the number of nights in the trip. The logic can be expanded with more advanced recommendations in future iterations.

## Assumptions Made

- **Travel Regions:**
  - Assumed the primary travel regions for the itineraries are Phuket and Krabi based on the project requirements.
  - No other regions are included in the current implementation.

- **Data Completeness:**
  - Assumed that all necessary data for the seed (hotels, activities, transfers) would be available for these regions.

- **API Request Handling:**
  - Assumed that all API requests would follow a valid format and input validation would handle invalid data gracefully.

## Challenges Faced and How They Were Resolved

1. **Issue with Relative Imports in Python:**
   - Initially encountered errors with relative imports when running certain scripts (e.g., `seed.py`).
   - Resolved by modifying the import statements to absolute imports or adjusting the `PYTHONPATH` to ensure that the app directory was properly recognized.

2. **Database Relationship Issues:**
   - Faced challenges while defining and ensuring correct relationships between models (e.g., ensuring the correct `One-to-Many` and `Many-to-One` relationships).
   - Resolved by reviewing SQLAlchemy documentation and testing the relationships with unit tests.

3. **API Testing and Validation:**
   - Encountered issues with API validation for complex data structures.
   - Solved by refining Pydantic model schemas and adding extra validation for nested models.

4. **Handling Data Seeding:**
   - Found that seeding data required careful attention to ensure the models were correctly referenced (e.g., foreign keys).
   - Addressed by testing the seeding process in isolated environments and ensuring relationships were correctly set.

## Conclusion

The project was successfully completed, implementing a functional backend system for managing travel itineraries with a relational database, API endpoints, and an MCP server for recommendations. The system is flexible and can be expanded to include additional features, such as more regions, advanced itinerary recommendations, and complex trip preferences.

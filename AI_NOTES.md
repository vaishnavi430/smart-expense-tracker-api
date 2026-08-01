# AI_NOTES.md

# AI Usage Notes

## AI Tools Used

- ChatGPT (OpenAI)

---

## 1. Which parts of the code were AI-generated vs. written by me?

### AI-assisted

I used ChatGPT as a learning assistant and coding guide throughout the project. AI helped me with:

- Designing the overall project structure.
- Explaining how to build REST APIs using FastAPI.
- Suggesting endpoint implementations for:
  - Add Expense
  - Get Expenses
  - Filter by Category
  - Expense Summary
  - Delete Expense
- Writing the initial unit test templates using Pytest.
- Creating the README.md structure.
- Creating this AI_NOTES.md document.

### Written and implemented by me

I personally:

- Created the project and folder structure.
- Set up the FastAPI application.
- Wrote and organized the project files.
- Integrated all suggested code into the project.
- Fixed import issues and runtime errors.
- Configured Git and GitHub.
- Tested every API endpoint using Swagger UI.
- Executed and verified all unit tests.
- Managed the JSON file storage.
- Reviewed and cleaned the final project before submission.

---

## 2. What did I validate, test, or change in the AI output?

I did not copy AI-generated code without verification.

I:

- Fixed import-related issues during development.
- Corrected endpoint placement and routing issues.
- Verified that each endpoint behaved correctly using Swagger UI.
- Confirmed that all CRUD operations worked with the JSON storage.
- Executed the full Pytest test suite and ensured all tests passed.
- Removed unused files from the project to keep the repository clean.
- Verified installation, execution, and testing commands before submission.

---

## 3. AI suggestions I decided not to use

During development, AI suggested a few improvements that I chose not to include because they were unnecessary for the scope of this assignment.

These included:

- Using a database such as SQLite instead of a JSON file.
- Implementing dependency injection and a service layer.
- Adding authentication and authorization.
- Creating separate configuration files and environment variables.
- Adding advanced logging and custom exception handlers.

I decided not to implement these because the assignment explicitly allowed local JSON storage and focused on a simple REST API implementation.

---

## Final Note

AI was used as a development assistant to explain concepts, suggest implementations, and review code. I independently integrated, tested, debugged, and validated the final application to ensure it met all assignment requirements.
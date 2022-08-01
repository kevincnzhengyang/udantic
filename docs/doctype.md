# Doctype
Doctype which is an core concept in [Frappe](https://frappeframework.com/) hereinafter is simply meaning the class of Docuemnt. And the Document hereinafter is the metadata which is:
- used to exchange information between a user and the "system" through the GUI,
- the JSON data transported between backend to frontend
- represented a specific "Data Model" in a user's operation context.

Doctype is responsible for:
- parse and validate JSON comes from the user's input to get a pydantic object
- manipulate and export a pydantic object to JSON


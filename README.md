# Medics

Medics is a Django-based web application for managing medical product inventory, vendors, and shop transactions. It includes modules for admin management, vendor interaction, and e-commerce-like shop operations with integrated Paytm payment support.

## Features

- Admin dashboard for managing medical products and vendors
- Vendor-specific portal for product management
- Shopfront for users to browse and purchase items
- Integrated Paytm payment gateway
- Image/media upload and management
- Django ORM-based models with forms and filters

## Project Structure

```
MedicsAdmin/
├── Medics/              # Core project settings and configuration
├── MedicsAdminApp/      # Admin-facing application
├── MedicsVendor/        # Vendor-facing application
├── shop/                # Shop interface and logic
├── Paytm/               # Payment gateway integration
├── manage.py            # Django entry point
├── db.sqlite3           # SQLite database
└── media/               # Uploaded media files
```

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/MedicsAdmin.git
   cd MedicsAdmin/MedicsAdmin
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   *(If `requirements.txt` is missing, install Django manually)*

   ```bash
   pip install django
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Access the app**

   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Notes

- Default database is SQLite for ease of setup.
- Make sure `media/` is writable for file uploads.
- You may need to extract `media.rar` manually if it includes additional resources.



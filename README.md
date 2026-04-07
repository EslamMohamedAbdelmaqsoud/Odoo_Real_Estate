# Real Estate Management System
Advanced Real Estate Management Module built with **Odoo 17**
## Overview
A comprehensive Real Estate Management application that provides complete solutions for managing properties, buildings, owners, clients, and related transactions. Built specifically for Odoo 17 to integrate seamlessly with your ERP system.
## Module: app_one
### Main Features
#### 📋 Core Models
- **Properties**: Complete property information management with tracking and history
- **Buildings**: Manage building information and relationships
- **Owners**: Owner information and property associations
- **Clients**: Client management and interactions
- **Tags**: Categorize and organize properties
- **Property History**: Track all property changes and modifications
- **Sales Integration**: Link sales orders with properties
- **Account Integration**: Connect accounting transactions to properties
#### 🎯 Key Capabilities
- ✅ Property lifecycle management
- ✅ Owner and client database
- ✅ Building classification and tracking
- ✅ Property tagging and categorization
- ✅ Sales order integration
- ✅ Financial transaction tracking
- ✅ Complete property history audit trail
- ✅ Custom state transitions via wizard
- ✅ XLSX reporting capabilities
- ✅ Multi-language support (Arabic included)
#### 📊 Reports & Analytics
- Property reports (PDF format)
- Advanced XLSX property reports with detailed analysis
- Property history tracking and reporting
#### 🔐 Security
- Row-level access control (RLS)
- Model-based access control
- User permission management via security groups
#### 🌍 Localization
- Arabic language support (ar_001)
- RTL (Right-to-Left) text support
- Multilingual interface support
#### 🎨 UI Enhancements
- Custom CSS styling for properties module
- Cairo font family integration for Arabic text
- Professional icon set
- Responsive design
#### 🔌 API
- RESTful API endpoints for property operations
- Test API endpoints for development
#### 📑 Data Management
- Sequence generation for property references
- Bulk operations support
- Data import/export capabilities
## Installation
1. **Copy the module** to your Odoo addons directory:
   ```bash
   cp -r custom_addons/app_one /path/to/odoo/addons/
   ```
2. **Update Apps List** in Odoo:
   - Go to Apps → Update Apps List
   - Click the Update Apps menu option
3. **Install the Module**:
   - Go to Apps → search for "app_one"
   - Click "Install"
4. **Activate Features**:
   - Navigate to the Real Estate menu
   - Start managing properties, owners, clients, and buildings
## Module Structure
```
app_one/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── property.py          # Main property model
│   ├── building.py          # Building management
│   ├── owner.py             # Owner information
│   ├── client.py            # Client information
│   ├── tag.py               # Property tags
│   ├── property_history.py  # Audit trail
│   ├── account_move.py      # Accounting integration
│   └── sale_order.py        # Sales integration
├── controllers/
│   ├── property_api.py      # Property REST API
│   └── test_api.py          # Test endpoints
├── views/
│   ├── property_view.xml    # Property forms and lists
│   ├── building_view.xml    # Building management
│   ├── owner_view.xml       # Owner forms
│   ├── client_view.xml      # Client management
│   └── ... (other views)
├── reports/
│   ├── property_report.xml  # PDF reports
│   └── xlsx_property_report.py # Excel reports
├── wizard/
│   └── change_state_wizard.py  # State management
├── security/
│   ├── ir.model.access.csv  # Access control
│   └── security.xml         # Security groups
├── data/
│   └── sequence.xml         # Reference sequences
├── i18n/
│   ├── app_one.pot
│   └── ar_001.po            # Arabic translations
└── static/
    └── ... (CSS, fonts, icons)
```
## Usage
### Creating a Property
1. Go to **Real Estate** → **Properties**
2. Click **Create**
3. Fill in the property details:
   - Property name and reference
   - Building and owner information
   - Property details (size, price, etc.)
   - Tags and categorization
4. Click **Save**
### Managing Buildings
1. Go to **Real Estate** → **Buildings**
2. Add, update, or delete buildings
3. Associate buildings with properties
### Owner & Client Management
1. Navigate to **Real Estate** → **Owners** or **Clients**
2. Maintain contact information
3. Track property associations
### Generating Reports
1. Open any property record
2. Click **Print** → select report format
3. Choose between PDF or XLSX format
## Requirements
- **Odoo**: Version 17.0 or higher
- **Python**: 3.8+
- **Dependencies**: Standard Odoo modules
## Configuration
The module requires:
- Proper access rights configuration
- Sequence setup for property references
- Chart of accounts setup (for accounting integration)
- Sales configuration (for sales integration)
## Development
### Testing
```bash
python -m pytest custom_addons/app_one/tests/
```
### API Endpoints
- `GET /api/properties` - List all properties
- `POST /api/properties` - Create new property
- `GET /api/test` - Test endpoint
## Support & Documentation
For issues, feature requests, or questions:
- Check the module code documentation
- Review security files for access control information
- Consult the wizard files for workflow management
## Author
**Eslam Mohamed Abdelmaqsoud**
## License
This module is part of the Odoo Real Estate Management System.
## Version
**v1.0** - Initial Release for Odoo 17
---
**Last Updated**: April 2026
For more information about Odoo, visit: [https://www.odoo.com](https://www.odoo.com)

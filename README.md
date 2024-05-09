**API Documentation**

**Vendor Management API**

### Endpoints

#### Vendors

- **GET** `/api/vendors/`: List all vendors.
- **POST** `/api/vendors/`: Create a new vendor.
- **GET** `/api/vendors/{vendor_id}/`: Retrieve details of a specific vendor.
- **PUT** `/api/vendors/{vendor_id}/`: Update details of a specific vendor.
- **DELETE** `/api/vendors/{vendor_id}/`: Delete a specific vendor.
- **GET** `/api/vendors/{vendor_id}/performance/`: Retrieve performance metrics of a specific vendor.

#### Purchase Orders

- **GET** `/api/purchase_orders/`: List all purchase orders.
- **POST** `/api/purchase_orders/`: Create a new purchase order.
- **GET** `/api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- **PUT** `/api/purchase_orders/{po_id}/`: Update details of a specific purchase order.
- **DELETE** `/api/purchase_orders/{po_id}/`: Delete a specific purchase order.
- **POST** `/api/purchase_orders/{po_id}/acknowledge/`: Acknowledge a purchase order.

### Vendor Endpoints

#### List all vendors

**GET** `/api/vendors/`

#### Create a new vendor

**POST** `/api/vendors/`

#### Retrieve details of a specific vendor

**GET** `/api/vendors/{vendor_id}/`

#### Update details of a specific vendor

**PUT** `/api/vendors/{vendor_id}/`

#### Delete a specific vendor

**DELETE** `/api/vendors/{vendor_id}/`

#### Retrieve performance metrics of a specific vendor

**GET** `/api/vendors/{vendor_id}/performance/`

### Purchase Order Endpoints

#### List all purchase orders

**GET** `/api/purchase_orders/`

#### Create a new purchase order

**POST** `/api/purchase_orders/`

#### Retrieve details of a specific purchase order

**GET** `/api/purchase_orders/{po_id}/`

#### Update details of a specific purchase order

**PUT** `/api/purchase_orders/{po_id}/`

#### Delete a specific purchase order

**DELETE** `/api/purchase_orders/{po_id}/`

#### Acknowledge a purchase order

**POST** `/api/purchase_orders/{po_id}/acknowledge/`

### Permissions

- **GET** and **POST** requests for all endpoints are allowed for any user.

### Note

- Please ensure to provide valid data and authentication tokens when making requests to these endpoints.
- For POST requests, ensure to include the required fields in the request body.

Feel free to reach out if you have any questions or need further assistance.

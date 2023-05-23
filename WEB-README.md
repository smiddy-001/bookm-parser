This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
```

To run the backend development server:

```bash
cd website && ./pocketbase serve
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

# Backend Bullshit

## config json

Here are a few commands to fetch and push data to each category in **Python**:

Fetching data from the `Imports` category:

```python
import json

# Load the JSON data from a file
with open('data.json', 'r') as f:
    data = json.load(f)

# Get the value of 'BmToCsv' in the 'Imports' category
bm_to_csv_path = data['Imports']['BmToCsv']
```

Pushing data to the `Unedited` category:

```python
import json

# Load the JSON data from a file
with open('data.json', 'r') as f:
    data = json.load(f)

# Add a new key-value pair to the 'Unedited' category
data['Unedited']['NewFile'] = 'new_file'

# Save the updated JSON data to a file
with open('data.json', 'w') as f:
    json.dump(data, f)
```

Here are a few commands to fetch and push data to each category in **JavaScript**:

Fetching data from the `Css` category:

```javascript
fetch("data.json")
  .then((response) => response.json())
  .then((data) => {
    // Get the value of 'White' in the 'Css' category
    const white = data.Css.White;
  });
```

Pushing data to the `Edited` category:

```javascript
fetch("data.json")
  .then((response) => response.json())
  .then((data) => {
    // Add a new key-value pair to the 'Edited' category
    data.Edited.NewOutput = "new_output";

    // Update the JSON data on the server
    fetch("update_data.php", {
      method: "POST",
      body: JSON.stringify(data),
    });
  });
```

Note that the above JavaScript commands assume that the JSON data is being served from a server and that the server has an API endpoint for updating the data.

## userdata json / bookmarks data

curl -H "Content-Type: application/json" \
     -d '{"type":"issue","title":"Send message", "description":"Let pilots.."}' \
     http://localhost:5000/create

curl -H "Content-Type: application/json" \
     -d '{"type":"bug","description":"cookpit ..", "description":"Let pilots.."}' \
     http://localhost:5000/create

curl -H "Content-Type: application/json" \
     -d '{"type":"task","title":"Clean rocket", "category":"maintenance"}' \
     http://localhost:5000/create
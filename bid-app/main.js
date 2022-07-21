let loginBtn = document.getElementById("login-btn");
let logoutBtn = document.getElementById("logout-btn");
let token = localStorage.getItem("token");
if (token) {
  loginBtn.remove();
} else {
  logoutBtn.remove();
}
logoutBtn.addEventListener("click", (e) => {
  e.preventDefault();
  localStorage.removeItem("token");
  window.location = "file:///C:/Users/parve/Desktop/bid-app/login.html";
});
let auctionUrl = "http://127.0.0.1:8000/api/bids/";
let getAuctions = () => {
  fetch(auctionUrl)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      buildAuction(data);
    });
};

let buildAuction = (auctions) => {
  let auctionWrapper = document.getElementById("auction--wrapper");
  for (let i = 0; auctions.length > i; i++) {
    let auction = auctions[i];
    let auctionCard = `
    <div class="auction--card">
    <img src="http://127.0.0.1:8000${auction.item_image}"

    <div>
        <div class="card--header">
            <h3>Item Name:${auction.item_name}</h3>
            <h6>Highest Bid ${auction.highbid}</h6>
            <h3>End date: <i>${auction.enddate}</i></h3>
            <div class="bid--input">
                    <input type="number" class="form-control bidvalue "   placeholder="Enter Amount">
                    <button type="submit"  data-auction="${auction.id}" class="btn btn-primary bidbtn">Submit</button>
            </div>
            <p>${auction.item_detail.substring(0, 100)}</p>
        </div>
        
    </div>
    </div>
    `;
    auctionWrapper.innerHTML += auctionCard;
  }
  bidsend();
};
let bidsend = () => {
  let btnvalue = document.getElementsByClassName("bid--input");
  let bidbtn = document.getElementsByClassName("bidbtn");
  let bidvalue = document.getElementsByClassName("bidvalue");
  for (let i = 0; btnvalue.length > i; i++) {
    bidbtn[i].addEventListener("click", (e) => {
      let auctionid = e.target.dataset.auction;

      console.log(bidvalue[i].value);
      fetch(`http://127.0.0.1:8000/api/bids/${auctionid}/raisebid/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ amount: bidvalue[i].value }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success", data);
        });
    });
  }
};
getAuctions();

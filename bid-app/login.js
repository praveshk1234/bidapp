let form = document.getElementById("login-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let formdata = {
    username: form.username.value,
    password: form.password.value,
  };
  fetch("http://127.0.0.1:8000/api/auction/token/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formdata),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("DATA:", data.access);
      if (data.access) {
        localStorage.setItem("token", data.access);
        window.location = "file:///C:/Users/parve/Desktop/bid-app/project-list.html";
      } else {
        alert("username OR passwork did not work");
      }
    });
  console.log("FORM DATA", formdata);
});

    const list = document.getElementById("itemList");
    const displayImg = document.getElementById("displayImg");

    list.addEventListener("mouseover", function(e) {
      if (e.target && e.target.nodeName === "LI") {
        // get the img path from data attribute
        const imgPath = e.target.getAttribute("data-img");
        displayImg.src = imgPath;
        displayImg.style.display = "block";
      }
    });

    list.addEventListener("mouseleave", function() {
      displayImg.style.display = "none"; // hide image when not hovering
    });
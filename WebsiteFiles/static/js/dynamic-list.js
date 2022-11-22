
		const ul = document.querySelector(".list-parent");
		// backtick here `````````````````````````````````
		let listData = [
        'Blue',
        'lol',
        'White',
        'Green',
        'Black',
        'Orange'
    	];
		let itemImg = ["https://cdn.icon-icons.com/icons2/2699/PNG/512/walmart_logo_icon_170230.png",
	"https://e7.pngegg.com/pngimages/156/169/png-clipart-target-logo-target-corporation-logo-target-icon-logo-text-retail.png",
"https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Stater_Bros.svg/1200px-Stater_Bros.svg.png"]

		// we gonna have a list of itemName, itemIMG, itemDesc, itemPrice
		for ( i = 0; i < listData.length; i++)
		{
		ul.innerHTML += `
		<li class="items-list">
	<img src= ${itemImg[i%3]} alt="icon" width="200" height="auto" />
		<!--Item image url goes here-->
	<div class="righttxt">
		<div class="Item-name"> 
			${listData[i]} <!--Item name goes here-->
		</div>
		<div class="Description"> 
			${listData[i]}  <!--Item description goes here-->
		</div>
		<div class="row">
			<div class="column">
			  <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/walmart_logo_icon_170230.png" alt="logo" width = "100" height = "auto">
			   <figcaption>$1.50</figcaption> <!--price for dif store-->
			</div>
			<div class="column">
			  <img src="https://e7.pngegg.com/pngimages/156/169/png-clipart-target-logo-target-corporation-logo-target-icon-logo-text-retail.png" alt="logo" width = "100" height = "auto">
			  <p>$2.00</p>
			</div>
			<div class="column">
			  <img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Stater_Bros.svg/1200px-Stater_Bros.svg.png" alt="logo" width = "100" height = "auto">
			  <p>$1.50</p>
			</div>
		</div>	
	</div>
	</li>
			`;
}
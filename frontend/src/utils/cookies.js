import useMainStore from "@/stores/main";

export default {
  getCookie(name) {
    let value = `; ${document.cookie}`;
    let parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
  },
  setCartCookie(item) {
    const currentCookie = this.getCookie("cartItems");
    let newCookie = [];
    if (currentCookie) {
      this.deleteCookie("cartItems");
      let isAdded = false;
      const parsedArray = JSON.parse(currentCookie);
      parsedArray.forEach((el) => {
        if (el.id === item.id) {
          el.count += item.count;
          isAdded = true;
        }
      });
      if (!isAdded) {
        parsedArray.push(item);
      }
      newCookie = parsedArray;
    } else {
      newCookie.push(item);
    }
    const store = useMainStore();
    store.setCartItems(newCookie);
    document.cookie = `cartItems=${JSON.stringify(newCookie)};max-age=${
      60 * 60 * 24 * 14
    };path=/;`;
  },
  deleteCookie(name) {
    document.cookie = `${name}=delete; path=/; max-age=0;`;
  },
  changeCartItem(item) {
    const currentCookie = JSON.parse(this.getCookie("cartItems"));
    const filteredCookieArray = currentCookie.filter((el) => el.id !== item.id);
    if (item.count !== 0) {
      filteredCookieArray.push(item);
    }
    this.deleteCookie("cartItems");
    const store = useMainStore();
    store.setCartItems(filteredCookieArray);
    document.cookie = `cartItems=${JSON.stringify(
      filteredCookieArray
    )};max-age=${60 * 60 * 24 * 14};path=/;`;
  },
};

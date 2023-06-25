import './App.css';
import InitPage from "./pages/InitPage";
import logo from "./images/logo.svg"
import image1 from "./images/image1.svg"
import image2 from "./images/image2.svg"
import image3 from "./images/image3.svg"
import fon from "../src/images/svg_fon.svg"

function App() {
    return (
        <div className="App">
            <img style={{width: 1224, height: 162, marginTop: "80px"}} src={logo}/>
            <InitPage/>
            <footer className="App-footer">
                <img className={"image"} src={image1}/>
                <img className={"image"} src={image2}/>
                <img className={"image"} src={image3}/>
            </footer>
        </div>
    );
}

export default App;

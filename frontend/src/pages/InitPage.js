import React, {useState} from 'react';
import {Button} from "@mui/material";
import useStyles from "./styles";
import FileUpload from "../components/FileUpload/FileUpload";
import DataScreen from "../components/DataScreen/DataScreen";

const InitPage = () => {

    const classes = useStyles();
    const [stateScreen, setStateScreen] = useState(0)
    const [data, setData] = useState(null)
    const [link, setLink] = useState(null)

    return (
        <div style={{display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center"}}>
            {stateScreen === 0 &&
                <FileUpload setStateScreen={setStateScreen} setData={setData} setLink={setLink}/>
            }
            {stateScreen === 1 &&
                <DataScreen setStateScreen={setStateScreen} data={data} link={link}/>
            }
        </div>
    );
};

export default InitPage;


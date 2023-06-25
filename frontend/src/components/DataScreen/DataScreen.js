import React, {useEffect, useState} from 'react';
import useStyles from "./styles";
import {Button} from "@mui/material";
import iconBack from "../../images/IconBack.svg"
import TableCsv from "../TableCsv/TableCsv";

const DataScreen = (props) => {

    const classes = useStyles();
    const [content, setContent] = useState(null)

    useEffect(() => {
        if(props.data !== null){
            let data = props.data
            data = data.split("\n")
            let arrayOfArrays = data.map(str => str.split(','));
            arrayOfArrays.splice(11, 1)
            setContent(arrayOfArrays)
        }
    }, [])

    function downloadData(){
        const blob = new Blob([props.data], { type: "text/csv" });
        // Создание ссылки для скачивания файла
        const downloadLink = document.createElement("a");
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = "answer.csv";
        downloadLink.click();
    }

    function goToBack(){
        props.setStateScreen(0)

    }

    return (
        <div className={classes.container}>
            <div className={classes.titleContainer}>
                <img onClick={goToBack} src={iconBack} className={classes.imgContainer}/>
                <div style={{display: "flex", flexDirection: "row", justifyContent: "center", alignItems: "center"}}>
                    <Button onClick={downloadData} style={downloadButton}>
                        Скачать обработанный датасет
                    </Button>
                </div>
            </div>
            {!!content &&
                <TableCsv data={content}/>
            }
        </div>
    );
};

export default DataScreen;

let downloadButton = {
    marginTop: 20,
    marginBottom: 20,
    background: "#00F43A",
    borderRadius: "20px",
    fontFamily: 'Nunito',
    fontStyle: "normal",
    fontWeight: 600,
    fontSize: "16px",
    lineHeight: "33px",
    color: "#181818",
    marginLeft: "15vw",
    height: "6vh"
}

import React, {useEffect, useState} from 'react';
import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";

const TableCsv = (props) => {

    const [head, setHead] = useState([])
    const [rows, setRows] = useState([])

    useEffect(() => {
        let new_data = props.data
        setRows(new_data)
    }, [props.data])

    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableBody>
                    {props.data.map((row, index) => (
                        <TableRow
                            key={row.name}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF", background: "#272727"}}>{row[1]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}} >{row[5]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}}>{row[17]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}}>{row[6]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}}>{row[7]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}}>{row[11]}</TableCell>
                            <TableCell align={index ? "right" : "center"} style={{color: "#FFFFFF",background: "#272727"}}>{row[9]}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
};

export default TableCsv;

let cellStyle = {
    background: "#272727",
}

import React, { useState } from 'react'
import { Text,View,StyleSheet, Dimensions, TouchableOpacity } from 'react-native'
import { bgDark, btnBg, centerElem, inputBg, opText } from '../constants/constants'
import FontAwesomeIcon from 'react-native-vector-icons/Ionicons'
const windowWidth=Dimensions.get('window').width
const windowHeight=Dimensions.get('window').height

export const MainScreen=()=>{
    const [mode,setMode]=useState(1)
    const [expression,setExpression]=useState('')
    const [result,setResult]=useState('')
    const [expOpacity,setExpOpacity]=useState(1)
    const keys=[1,2,3,4,5,6,7,8,9,0,'+','-','/','*','%','^','=','C']
    const [prevOper,setPrevOper]=useState('*')
    const calculateExpression=(elem)=>{ 
        if(!(keys.indexOf(elem)>10 && keys.indexOf(elem)<keys.length-2 && keys.indexOf(prevOper)>10 && keys.indexOf(prevOper)<keys.length-2)){
            if(elem=='='){
                var s=eval(expression)
                setResult(s)
                setExpOpacity(0.5)
                
            }else if(elem=='C'){
                setExpression('')
                setResult('')
            }else{
                var s=expression
                s+=String(elem)
                setExpression(s)
            }
        }
        
        setPrevOper(elem)
    }
    const styles=StyleSheet.create({
        keyItem:{
            width:windowWidth*0.333,
            height:windowWidth*0.2,
            justifyContent:'center',
            backgroundColor:(mode==1)?inputBg:'white',
            textAlign:'center',
        },
        keyText:{
            ...centerElem,
            fontSize:30,
            color:(mode==1)?opText:'black',
        },  
        keyPad:{
            display:'flex',
            flexDirection:'row',
            flexWrap:'wrap',
            justifyContent:'flex-end',
            width:windowWidth,
            backgroundColor:(mode==1)?bgDark:'gray'
        },
        valueDisplay:{
            height:windowHeight*0.401
        },
        mainScreen:{
            backgroundColor:(mode==1)?bgDark:null,
    
        },
        calcText:{
            color:(mode==1)?opText:'black',
            fontSize:50,
            marginTop:'auto',
            marginLeft:'auto',
            marginHorizontal:15,
            opacity:expOpacity
        },
        resultText:{
            color:(mode==1)?opText:'black',
            fontSize:70,
            marginLeft:'auto',
            marginHorizontal:15
        }
    })
    return(
        <View style={styles.mainScreen}>
            <FontAwesomeIcon onPress={()=>setMode(!mode)} name={(mode==1)?'moon-outline':'sunny-outline'} color={(mode)?opText:inputBg} style={{margin:15, position:'absolute'}} size={(mode)?30:40}/>
            <View>
                <View style={styles.valueDisplay}>
                    <Text style={styles.calcText}>{expression}</Text>
                    <Text style={styles.resultText}>{result}</Text>
                </View>
            </View>
            <View style={styles.keyPad}>
            {
                keys.map(elem=><TouchableOpacity onPress={()=>{
                    calculateExpression(elem)
                }} style={styles.keyItem}><Text style={styles.keyText}>{elem}</Text></TouchableOpacity>)
            }
            </View>
           
        </View>
    )
}




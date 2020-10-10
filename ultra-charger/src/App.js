import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Grid, Segment } from 'semantic-ui-react'
import Map from './componets/Map'
import Sidebar from './componets/Sidebar'
import 'semantic-ui-css/semantic.min.css'

function App() {
  return (
    <div className="App">
        <Grid columns={2} stackable={false}>
          <Grid.Column width={4}>
          <Sidebar></Sidebar>
        </Grid.Column>
        <Grid.Column width={12}>
          <Map></Map>
        </Grid.Column>
      </Grid>      
    </div>
  );
}

export default App;

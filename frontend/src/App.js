import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
    totalPotentials : '',
    totalPipelines : '',
    totalChildAccount: '',
    maxValueableId: '',
    totalAccountsWon: '',
    accountName: '',
    endCustomer: ''
}
}

  componentWillMount() {
    console.log("Sending a GET API Call !!!");
    axios.get('/account_details/')
    .then(res => {
            this.setState({totalAccountsWon:res.data[0].totalAccountsWon})
            this.setState({totalChildAccount:res.data[0].totalChildAccount})
            this.setState({totalPipelines:res.data[0].totalPipelines})
            this.setState({totalPotentials:res.data[0].totalPotentials})
            this.setState({maxValueableId:res.data[0].maxValueableId})
    }).then(response => {
        console.log(JSON.stringify(response));
    }) 

    axios.get('/account_risk_details/')
    .then(res => {
            console.log('my data ',res.data.length)

            for(var i=0; i< res.data.length;i++) {
                 if(res.data[i].account_id === this.state.maxValueableId) {
                      this.setState({accountName:res.data[i].account_name})
                      this.setState({endCustomer:res.data[i].customer_name})
                 }
            }
            // this.setState({totalAccountsWon:res.data[0].totalAccountsWon})
            // this.setState({totalChildAccount:res.data[0].totalChildAccount})
            // this.setState({totalPipelines:res.data[0].totalPipelines})
            // this.setState({totalPotentials:res.data[0].totalPotentials})
            // this.setState({maxValueableId:res.data[0].maxValueableId})
    }).then(response => {
        console.log(JSON.stringify(response));
    }) 

  }

  // onClickAccount(ev) {
  //   console.log("Sending a GET API Call !!!");
  //   axios.get('/account_details/')
  //   .then(res => {
  //           console.log(res.data)
  //   }).then(response => {
  //       console.log(JSON.stringify(response));
  //   })    
  // } 

  onClickAccountRisk(ev) {
    console.log("Sending a GET API Call !!!");
    axios.get('/account_risk_details/')
    .then(res => {
            console.log(res.data)
    }).then(response => {
        console.log(JSON.stringify(response));
    })    
  } 

  render() {
    return (
      <div class="app">
      <div class="row">
           <div class="col-sm-3">
           <div class="btn-box">
            <h3>{this.state.totalChildAccount}</h3>
          <div class="col-md-12">
            <div class="body trim-text">
              <p>CHILD ACCOUNTS
              </p>
            </div>
          </div>
        </div>
           </div>

           <div class="col-sm-3">
           <div class="btn-box">
           <h3>{this.state.totalAccountsWon}</h3>
            <div class="col-md-12">
              <div class="body trim-text">
                <p>ACCOUNTS WON
                </p>
              </div>
            </div>
          </div>
           </div>
           
           <div class="col-sm-3">
           <div class="btn-box">
           <h3>{this.state.totalPotentials}</h3>
            <div class="col-md-12">
              <div class="body trim-text">
                <p>HIGH POTENTIAL ACCOUNTS
                </p>
              </div>
            </div>
          </div>
           </div>

           <div class="col-sm-3">
           <div class="btn-box">
           <h3>{this.state.totalPipelines}</h3>
            <div class="col-md-12">
              <div class="body trim-text">
                <p>HIGH PIPELINE ACCOUNTS
                </p>
              </div>
            </div>
          </div>
           </div>
      </div>
      <div class="row txt-row">
         <p> * All the account references are for child accounts
           </p>
      </div>
      <div class="row mid-cls">
      <div class="top-box">
      <div class="col-md-12 top-icon">
      <span class="high-pipeline"> High Pipeline
        </span>
        <span>      </span> 
        <span class="high-pipeline"> High Potential
        </span>
      </div>
       <div class="acc-name-row">
         <div class="col-md-12 acc-name">
         <p> ACCOUNT NAME : {this.state.accountName}
           </p>
         </div>
         <div class="col-md-12 acc-name">
         <p> END CUSTOMER : {this.state.endCustomer}
           </p>
         </div>
         </div>
      </div>
      <div class="col-md-12">
         <div class="row">
         <div class="col-md-4 acc-risk">
             Account Risk (s)
         </div>
         <div class="col-md-8">
            <ul class="a">
               <li>26% of the pipe is ageing</li>
               <li>Accounts margins are lower and deal discounts are higher than average of similar accounts. </li>
              <li>Annual revenues from the accounts are declining.</li>
              <li>Account has lower cloud coverage than similar accounts.</li>
               <li>Competitive win ratio against Dell-EMC is low</li>
            </ul>
           </div>
         </div>
        </div>
      </div>
      </div>
    );
  }

}

export default App;

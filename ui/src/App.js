import React, { Component } from 'react';
import './App.css';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.css';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      formData: {
        radius: '',
        texture: '',
        perimeter: '',
        area: '',
        smoothness: '',
        compactness: '',
        concavity: '',
        concavepoints: '',
        symmetry: '',
        fractaldimensions: ''
      },
      result: ""
    };
  }

  handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    var formData = this.state.formData;
    formData[name] = value;
    this.setState({
      formData
    });
  }

  handleDiagnoseClick = (event) => {
    const formData = this.state.formData;
    this.setState({ isLoading: true });
    fetch('http://127.0.0.1:5000/diagnosis/', 
      {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(formData)
      })
      .then(response => response.json())
      .then(response => {
        this.setState({
          result: response.result,
          isLoading: false
        });
      });
  }

  handleResetClick = (event) => {
    this.setState({ result: "" });
    this.setState({
      isLoading: false,
      formData: {
        radius: '',
        texture: '',
        perimeter: '',
        area: '',
        smoothness: '',
        compactness: '',
        concavity: '',
        concavepoints: '',
        symmetry: '',
        fractaldimensions: ''
      },
      result: ""
    });
  }

  render() {
    const isLoading = this.state.isLoading;
    const formData = this.state.formData;
    const result = this.state.result;

    return (
      
      <Container className = "backGround">
        <div className="titleBox">
          <h1 className="title">Breast Cancer Cell Classifier</h1>
        </div>
        <div className="content">
          <Form>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Radius</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="radius"
                  value={formData.radius}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Texture</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="texture"
                  value={formData.texture}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Perimeter</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="perimeter"
                  value={formData.perimeter}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Area</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="area"
                  value={formData.area}
                  onChange={this.handleChange} />
              </Form.Group>
            </Form.Row>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Smoothness</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="smoothness"
                  value={formData.smoothness}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Compactness</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="compactness"
                  value={formData.compactness}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Concavity</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="concavity"
                  value={formData.concavity}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Concave Points</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="concavepoints"
                  value={formData.concavepoints}
                  onChange={this.handleChange} />
              </Form.Group>
            </Form.Row>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Symmetry</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="symmetry"
                  value={formData.symmetry}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Fractal Dimensions</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="0.0"
                  name="fractaldimensions"
                  value={formData.fractaldimensions}
                  onChange={this.handleChange} />
              </Form.Group>
            </Form.Row>
            <Row>
              <Col>
                <Button
                  block
                  disabled={isLoading}
                  onClick={!isLoading ? this.handleDiagnoseClick : null}>
                  {isLoading ? 'Making diagnosis' : 'Diagnose'}
                </Button>
              </Col>
              <Col>
                <Button
                  block
                  disabled={isLoading}
                  onClick={this.handleResetClick}>
                  Reset
                </Button>
              </Col>
            </Row>
          </Form>
          {result === "" ? null :
            (<Row>
              <Col className="result-container">
                <h5 id="result">{result}</h5>
              </Col>
            </Row>)
          }
        </div>
      </Container>
    );
  }
}

export default App;

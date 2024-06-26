import { styled, keyframes } from "styled-components";
import React, {
  useCallback,
  useState,
  useRef,
  useEffect,
  useContext,
} from "react";
import leaningman_right from "../../images/leaningmanright.png";
import { Col, Button, Row, Container, Card, Form } from "react-bootstrap";
import leaningman_left from "../../images/leaningmanleft.png";
import Alert from "../../components/Alert";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";
import Student from "./Student";
import Spinner from "react-bootstrap/Spinner";
import StudentPanelContext from "./StudentPanelContext";

const MainDiv = styled.div`
  width: 100%;
  min-height: 100%;
  height: 100%;
  position: relative;
  .size {
    height: 0px;
    width: 100%;
    margin-bottom: 100px;
    padding: 10px;
  }
  @media screen and (max-width: 800px) {
    .size {
      padding: 4px;
    }
  }
`;

export default function GetStudents() {
  const [students, setStudents] = useState([]);
  const { loading, setLoading } = useContext(StudentPanelContext);
  const location = useLocation();

  useEffect(() => {
    if (!location.state) {
      return;
    }
    setLoading(true);
    axios
      .get(
        `http://178.239.151.92:8000/register/studentInfo/${location.state.username}/${location.state.password}/`
      )
      .then((res) => {
        setStudents([res.data]);
        setLoading(false);
      });
    // .catch((err) => console.log(err));
  }, []);

  return (
    <MainDiv>
      <div className="size">
        <Container className="p-0" fluid>
          {students.map((student) => (
            <Student
              student={student}
              setStudents={setStudents}
              key={student.id}
            />
          ))}
          {students.length == 0 && !loading && (
            <h1 style={{ margin: "auto" }}>{"دانش آموز ای موجود نیست"}</h1>
          )}
        </Container>
      </div>
    </MainDiv>
  );
}

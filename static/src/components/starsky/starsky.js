import React, { Component } from 'react';
import './starsky.scss'
import WarpDrive from '../../asserts/warpdrive.js'



const settings = {
    width: 480,
    height: 480,
    autoResize: true,
    autoResizeMinWidth: null,
    autoResizeMaxWidth: null,
    autoResizeMinHeight: null,
    autoResizeMaxHeight: null,
    addMouseControls: true,
    addTouchControls: true,
    hideContextMenu: true,
    starCount: 6666,
    starBgCount: 2222,
    starBgColor: { r: 0, g: 204, b: 255 },
    starBgColorRangeMin: 20,
    starBgColorRangeMax: 80,
    starColor: { r: 0, g: 204, b: 255 },
    starColorRangeMin: 50,
    starColorRangeMax: 100,
    starfieldBackgroundColor: { r: 5, g: 5, b: 14 },
    starDirection: 1,
    starSpeed: 20,
    starSpeedMax: 200,
    starSpeedAnimationDuration: 2,
    starFov: 300,
    starFovMin: 200,
    starFovAnimationDuration: 2,
    starRotationPermission: true,
    starRotationDirection: 1,
    starRotationSpeed: 0.0,
    starRotationSpeedMax: 1.0,
    starRotationAnimationDuration: 2,
    starWarpLineLength: 2.0,
    starWarpTunnelDiameter: 100,
    starFollowMouseSensitivity: 0.025,
    starFollowMouseXAxis: true,
    starFollowMouseYAxis: true

};

class Starsky extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        var warpdrive_inst = new WarpDrive(document.getElementsByClassName('starsky')[0], settings);
    }
    render() {
        return (
            <div className='starsky'>
            </div>
        );
    }
}

export default Starsky
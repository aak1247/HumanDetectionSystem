import React, { Component } from 'react';
import './Model.scss'

class Model extends Component {
    render() {
        return (
            <div className='model'>
                <div>模型状态</div>
                <div>空闲中</div>
                <div>当前待分析任务数</div>
                <div>预计完成时长</div>
                <div>重新训练</div>
                <div>回滚至日期</div><div>picker</div>
            </div>
        );
    }
}

export default Model
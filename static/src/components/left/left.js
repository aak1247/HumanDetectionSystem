import React, { Component } from 'react';
import SwipeableDrawer from '@material-ui/core/SwipeableDrawer';
import Drawer from '@material-ui/core/Drawer';
import Divider from '@material-ui/core/Divider';
import './left.scss'


class Left extends Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }

    render() {
        const { listItems, isOpen, troggleFunc } = this.props;
        return (
            <SwipeableDrawer
                open={isOpen}
                onClose={troggleFunc}
                onOpen={troggleFunc}
                anchor='left'>
                <div className="left">
                    {listItems}
                </div>
            </SwipeableDrawer>
        )
    }
}

export default Left
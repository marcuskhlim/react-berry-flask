import React, { useState } from 'react';

// material-ui
import { Typography } from '@material-ui/core';

// project imports
import MainCard from '../../ui-component/cards/MainCard';

import Button from '../../ui-component/Button';
import SelectBox from '../../ui-component/SelectBox';
import TextBox from '../../ui-component/TextBox';

import { postGenerateTextEndpoint } from '../../utils/async';

import configData from '../../config';

import axios from 'axios';


//==============================|| SAMPLE PAGE ||==============================//

const SamplePage = () => {
  const [text, setText] = useState("");
  const [model, setModel] = useState('gpt2');
  const [generatedText, postGenerateText] = postGenerateTextEndpoint('cold-emails');

  const generateText = () => {
    postGenerateText({ text, model, userId: 1 });
  }    
    return (
        <MainCard title="Sample Card">
        {/*
            <Typography variant="body2">
                Lorem ipsum dolor sit amen, consenter nipissing eli, sed do elusion tempos incident ut laborers et doolie magna alissa. Ut
                enif ad minim venice, quin nostrum exercitation illampu laborings nisi ut liquid ex ea commons construal. Duos aube grue
                dolor in reprehended in voltage veil esse colum doolie eu fujian bulla parian. Exceptive sin ocean cuspidate non president,
                sunk in culpa qui officiate descent molls anim id est labours.
            </Typography>

        */}

              <form className="aiform" noValidate autoComplete='off'>
        <h1>React GPT</h1>
        <SelectBox model={model} setModel={setModel} />
        <TextBox text={text} setText={setText} />
        <Button onClick={generateText} />
      </form>

      {generatedText.pending &&
        <div className='result pending'>Please wait</div>}

      {generatedText.complete &&
        (generatedText.error ?
          <div className='result error'>Bad Request</div> :
          <div className='result valid'>
            {generatedText.data.result}
          </div>)}
   

        </MainCard>

    );
};

export default SamplePage;

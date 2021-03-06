import tensorflow as tf
import numpy as np

g = tf.Graph()
with g.as_default():
    init_state_fw = tf.constant([[0, 0]], tf.float32, [1, 2], 'init_state_fw')
    init_state_bw = tf.constant([[0, 0]], tf.float32, [1, 2], 'init_state_bw')

    seqs = tf.constant(
        [
            [[1, 1], [2, 2], [3, 3]],
        ],
        tf.float32,
        [1, 3, 2],
        'seqs'
    )
    
    seq_len = tf.constant(
        [
            2,
        ],
        tf.int32,
        [1]
    )
    
    with tf.variable_scope('fw'):
        cell_fw = tf.contrib.rnn.BasicRNNCell(2, tf.tanh)

    with tf.variable_scope('bw'):
        cell_bw = tf.contrib.rnn.BasicRNNCell(2, tf.tanh)
        
    ((outputs_fw, outputs_bw), (state_fw, state_bw)) = tf.nn.bidirectional_dynamic_rnn(cell_fw, cell_bw, seqs, sequence_length=seq_len, initial_state_fw=init_state_fw, initial_state_bw=init_state_bw)
    
    outputs = tf.concat([ outputs_fw, outputs_bw ], axis=2)
    state = tf.concat([ state_fw, state_bw ], axis=1)
    
    init = tf.global_variables_initializer()
    
    g.finalize()

    with tf.Session() as s:
        s.run([ init ], { })
        
        [
            curr_outputs_fw, curr_outputs_bw, curr_outputs,
            curr_state_fw, curr_state_bw, curr_state
        ] = s.run([
            outputs_fw, outputs_bw, outputs,
            state_fw, state_bw, state
        ], { })

        print('-------------')
        print('curr_outputs_fw')
        print(curr_outputs_fw)
        print()
        
        print('-------------')
        print('curr_outputs_bw')
        print(curr_outputs_bw)
        print()
        
        print('-------------')
        print('curr_outputs')
        print(curr_outputs)
        print()
        
        print('-------------')
        print('curr_state_fw')
        print(curr_state_fw)
        print()
        
        print('-------------')
        print('curr_state_bw')
        print(curr_state_bw)
        print()
        
        print('-------------')
        print('curr_state')
        print(curr_state)
        print()

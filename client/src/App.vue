<template lang="pug">
  .pug-todo
    .todoPlace
      .addNewTaskPlace
        input(type="text" placeholder="Add new task" v-model="newTaskText")
        button(@click="addNewTask") Add

      .tasks
        taskComponent(v-for="task, index in tasks" :taskData="task" :key="index" @deleteTask="deleteTask(index)")
</template>



<script>
import taskComponent from './components/taskComponent.vue';
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return{
      newTaskText: '',
      tasks: [],
    };
  },

  components: {
    taskComponent
  },

  created(){
    this.getTasks();
  },

  methods:{

    getTasks(){
      const path = "http://localhost:5000/tasks";
      axios.get(path)
      .then((res)=>{
        this.tasks = res.data.tasks
      })
      .catch(error => {
        console.log(error)
      })
    },

    addNewTask(){
      const Data = {
        taskText: this.newTaskText.trim(),
      };

      if (Data.taskText == ""){
        alert("The field is empty!");
        return;
      }

      const path = "http://localhost:5000/tasks";
      axios.post(path, Data)
      .then((res) =>{
        console.log("Task created: ", res.data);
        this.newTaskText = "";
        this.getTasks();
      })
      .catch(error=>{
        console.error('Error creating task:', error);
        this.getTasks();
      })

      
    },

    deleteTask(index){
      const task_id = this.tasks[index].taskID;
      const path = 'http://localhost:5000/tasks/' + task_id;
      console.log(path);
      axios.get(path, task_id)
      .then((res) =>{
        console.log("Removed task ${task_id}", res);
        this.getTasks();
      })
      .catch(error =>{
        console.log("Error removed task: ", error);
        this.getTasks();
      })
    }
  }
}
</script>

<style lang="scss">
  body{
    margin:0;
    padding:0;
  }
  .pug-todo{
    display: flex;
    align-items: center;
    justify-content: center;
    background-color:blue;
    height:100vh;

    .todoPlace{
      width: 30%;
      
      background-color:white;
      border-radius:15px;
      padding:30px;


      .addNewTaskPlace{
        margin:30px 0px 60px;
        width: 100%;
        display:flex;

        input{
          border: 3px solid blue;
          border-radius: 7px;
          text-align: center;
          font-size: 2em;
          width: 70%;
        }

        button{
          margin-left: 20px;
          width: 30%;
          flex-grow: 1;
          background-color: blue;
          border: 3px solid blue;
          border-radius: 5px;
          text-align: center;
          font-size: 2em;
          color:white;
          cursor: pointer;
        }
      }

      .tasks{
        max-height: 300px;
        overflow-y: auto;
        overflow-x: hidden;
        padding-right:5px;
      }
    }
  }

</style>

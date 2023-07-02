<template lang="pug">
  .task
    .taskPlace
      .taskText
        span {{ taskData.taskText }}
      
      .removeButtonPlace(@click="deleteTask")
        .removeButton
          img(src="../assets/remove.png")

</template>
<script>
export default {
  name: 'taskComponent',
  props: ['taskData'],
  methods: {
    deleteTask(){
      this.$emit('deleteTask');
    }
  }
}
</script>

<style lang="scss">
  .taskPlace{
    width:100%;
    min-height: 60px;
    border-radius: 5px;
    border: 1px solid black;
    background-color:rgb(177, 255, 245);
    display: flex;
    align-items: center;
    font-size:1.5em;
    margin-bottom: 10px;

    .taskText{
      
      width:70%;
      margin-left: 20px;
      overflow-wrap: break-word;
    }

    .removeButtonPlace{
      width:30%;
      display:flex;
      justify-content: flex-end;

      .removeButton{
        width:40px;
        height:40px;
        background-color:blue;
        display:flex;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        margin-right: 10px;
        cursor:pointer;
        user-select: none;
        
        img{
          width:20px;
          height:20px;
          
        }
      }
    }
  }


</style>
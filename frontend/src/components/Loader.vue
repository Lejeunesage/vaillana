<template>
    <div class="dot-loader">
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<style>
.container {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-family: Helvetica;
}

.dot-loader {
  position: relative;
  background: #f7f4f4 ;
  width: 50px;
  height: 30px;
  border-radius: 30px;
}
@keyframes anim {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-5px);
  }
}
.dot-loader div:nth-child(1) {
  position: absolute;
  top: 16px;
  width: 8px;
  height: 8px;
  border-radius: 8px;
  background: #131111;
  animation: anim 0.5s ease alternate infinite;
  left: 10px;
}
.dot-loader div:nth-child(2) {
  position: absolute;
  top: 16px;
  width: 8px;
  height: 8px;
  border-radius: 8px;
  background: #131111;
  animation: anim 0.5s ease alternate infinite;
  left: 22px;
  animation-delay: 0.2s;
}
.dot-loader div:nth-child(3) {
  position: absolute;
  top: 16px;
  width: 8px;
  height: 8px;
  border-radius: 8px;
  background: #131111;
  animation: anim 0.5s ease alternate infinite;
  left: 34px;
  animation-delay: 0.3s;
}
</style>
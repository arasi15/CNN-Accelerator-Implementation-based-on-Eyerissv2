# CNN Accelerator Implementation based on Eyerissv2

This is a course project based on Verilog.    

I realized a CNN accelerator architecture based on Eyeriss v2 to progress convolution.

## RTL

- GLB_CLUSTER   
  - GLB_WGHT
  - GLB_IACT
  - GLB_PSUM

<img src="https://i.loli.net/2020/07/22/Gxrw8ALtJdFcs1R.png" alt="glb.png" style="zoom:60%;" div align=center />

- PE_CLUSTER   
- PE
  - SPad
  - MUX
  - MAC

<img src="https://i.loli.net/2020/07/22/S8M1aA5rZN9vkf7.png" alt="PE.png" style="zoom:67%;"  div align=center />

- ROUTER_CLUSTER    

  - ROUTER_IACT
  - ROUTER_WGHT
  - ROUTER_PSUM

<img src="https://i.loli.net/2020/07/22/wtIXlgcy3J4aedO.png" alt="image.png" style="zoom:67%;"  div align=center  />

- HMNOC

  - 4_CLUSTER

    - 1_CLUSTER

      <img src="https://i.loli.net/2020/07/22/5wtb3T94rMudgXe.png" alt="image.png" style="zoom:60%;" />

## SIMULATION

- 1_CLUSTER
  - HMNOC_1_CLUSTER_TB

<img src="https://i.loli.net/2020/07/22/7GcVkZ1Nov4AHsj.png" alt="image.png" style="zoom:67%;" />



- 4_CLUSTER
- HMNOC_4_CLUSTER_TB  

![image.png](https://i.loli.net/2020/07/22/arEVChcJLT4n7y1.png)

## Demo

### Average Filter

![image.png](https://i.loli.net/2020/07/22/kKtyZmIuOagoA7R.png)

### Result

![image.png](https://i.loli.net/2020/07/22/qfArH9kKJdIlRGW.png)

## Reference

1. {Y.-H. Chen, J. Emer, and V. Sze, “Eyeriss: A Spatial Architecture for Energy-Efficient Dataflow for Convolutional Neural Networks,” *ISCA*, 2016.}
2. {Y.-H. Chen, S. Member, T.-J. Yang, J. Emer, V. Sze, and S. Member, “Eyeriss v2: A Flexible Accelerator for Emerging Deep Neural Networks on Mobile Devices,” *ISCA*, 2019.}
3. https://github.com/karthisugumar/CSE240D-Hierarchical_Mesh_NoC-Eyeriss_v2

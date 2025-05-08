# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

I have chosen to implement our project using Azure Web Apps because it is more cost-effective in the long run. Azure Web Apps typically follow a pay-as-you-go pricing model, which can be more economical for smaller applications compared to Virtual Machines. This can lead to significant long-term savings, especially for projects that may start small but have the potential for growth. Additionally, with Azure Web Apps, we do not need to manage the underlying infrastructure, saving costs related to maintenance and management. 

In terms of scalability, Azure Web Apps offer built-in automatic scaling options that allow us to adjust resources based on traffic. This flexibility is advantageous as it enables us to start with a web app and focus on development and deployment without worrying about server management. If necessary, we can easily transition to a Virtual Machine in the future. This scalability can also help accommodate unexpected traffic spikes, which is common in web applications. 

Regarding availability, Azure Web Apps are designed for high availability with built-in redundancy and failover capabilities. Azure manages the infrastructure to ensure uptime, and they provide Service Level Agreements (SLAs) that guarantee a certain level of availability. Specifically, Azure provides an SLA of 99.99% uptime for Azure Web Apps, ensuring that our application remains accessible to users. This high level of availability is critical for user satisfaction, as downtime can lead to lost users and revenue. 

For the workflow, deploying to Azure Web Apps can be done through various methods such as GitHub Actions, Azure DevOps, or manual uploads, streamlining the development process. Azure also provides monitoring tools that help us track the performance of our web app, making it easier to maintain and optimize. Additionally, the ability to integrate with CI/CD (Continuous Integration/Continuous Deployment) tools enhances the development workflow, making it easier to implement updates and new features. 

In conclusion, by leveraging Azure Web Apps, we not only reduce costs but also enhance our ability to deliver a reliable and efficient application to our users. This approach provides the flexibility to scale and adapt as our project grows, contributing to the overall success of the project. Azure Web Apps allow for quick adjustments to meet changing project needs, ensuring that we can continue to deliver value to our users.

### Assess app changes that would change your decision.

If I were to consider deploying the application on a Virtual Machine instead of Azure Web Apps, several changes would need to be made. First, the application would require a more complex setup, as I would need to manage the operating system and install all necessary software, including web servers and databases. This would increase the workload for deployment and ongoing maintenance.

Additionally, using a Virtual Machine would provide greater control over the infrastructure, allowing for custom configurations tailored to specific application needs. However, this would also mean taking on the responsibility for security updates and scaling, which Azure Web Apps typically manage automatically.

To accommodate this change, I would also need to consider additional resources, such as a dedicated database server and possibly load balancers to manage traffic effectively. This shift would require careful planning and additional management efforts to ensure the application remains reliable and scalable.

# Lecture 12

**Infrastructure / cloud computing**

---

## Agenda

1. Technical stuff
1. Zooming out

---

## Infrastructure

There are whole certifications/careers on this stuff; we're just scratching the surface.

---

## Terms

What's a server?

---

- Workload
- Compute
- Memory
- Storage
  - Disk
  - Blob
- GPU
- Identity and access management (IAM)
  - Principals
- [Region](https://cloud.google.com/about/locations)

---

## Networking

### Local area network (LAN)

_Show wifi connection_

---

```sh
flask run --host 0.0.0.0
```

---

### Internet Protocol (IP) addresses

- IPv4
- IPv6

---

### Wide area network (WAN)

- `dig <domain>`
- [Whats My IP Address](https://whatismyipaddress.com/)

---

## VPN

- Why do people use them?
- What do they do?

---

### Virtual private cloud (VPC)

---

## Why cloud?

---

## Containers

- Like [virtual environments](https://docs.python.org/3/library/venv.html) with greater isolation+portability
- Docker
- Registry
- Kubernetes

---

## [Terraform](https://www.terraform.io/)

---

### Demo

1. Create a Project.
1. Grant everyone (`advanced-computing-for-policy-all@columbia.edu`) Viewer access.
1. Re-run.
1. Create a BigQuery dataset and table.
1. Change access to just the dataset.
1. Change the dataset name.

---

- Configuration as code (CaC)
- Infrastructure as code (IaC)

Why might these be useful?

---

Why are we talking about all of this? How does it relate to policy?

---

> The magic of law is now inextricably tied to the bits and bytes of computer code.

-Jennifer Pahlka, [Recoding America](https://www.recodingamerica.us/)

---

## [Readings](../readings/week_13.md)

They're heavy again this week, don't wait!

---

## [Reading response questions](https://edstem.org/us/courses/89925/discussion/7885181)

### Usability Testing for Dev Tools
- Are developers of tools like Google Cloud actually conducting usability testing for engineers, or is it assumed that technical users will adapt on their own?
- Does anyone actually usability-test DevOps tooling, or do we just assume engineers can figure it out?

---

### Cloud Computing & Data Centers
- How can organizations balance efficiency with the need to keep systems understandable and manageable for human users?
- As they [Big Tech companies] are expanding their business operations, and with AI in the picture, is this why building their own data centers makes more sense, rather than renting?

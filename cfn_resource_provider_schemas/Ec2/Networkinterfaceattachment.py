SCHEMA = {
  "typeName" : "AWS::EC2::NetworkInterfaceAttachment",
  "description" : "Attaches an elastic network interface (ENI) to an Amazon EC2 instance. You can use this resource type to attach additional network interfaces to an instance without interruption.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "properties" : {
    "AttachmentId" : {
      "description" : "",
      "type" : "string"
    },
    "DeleteOnTermination" : {
      "description" : "Whether to delete the network interface when the instance terminates. By default, this value is set to ``True``.",
      "type" : "boolean",
      "default" : True
    },
    "DeviceIndex" : {
      "description" : "The network interface's position in the attachment order. For example, the first attached network interface has a ``DeviceIndex`` of 0.",
      "type" : "string"
    },
    "InstanceId" : {
      "description" : "The ID of the instance to which you will attach the ENI.",
      "type" : "string"
    },
    "NetworkInterfaceId" : {
      "description" : "The ID of the ENI that you want to attach.",
      "type" : "string"
    },
    "EnaSrdSpecification" : {
      "$ref" : "#/definitions/EnaSrdSpecification",
      "description" : "Configures ENA Express for the network interface that this action attaches to the instance."
    }
  },
  "additionalProperties" : False,
  "replacementStrategy" : "delete_then_create",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "DeviceIndex", "InstanceId", "NetworkInterfaceId" ],
  "readOnlyProperties" : [ "/properties/AttachmentId" ],
  "createOnlyProperties" : [ "/properties/DeviceIndex", "/properties/InstanceId", "/properties/NetworkInterfaceId" ],
  "primaryIdentifier" : [ "/properties/AttachmentId" ],
  "additionalIdentifiers" : [ [ "/properties/NetworkInterfaceId" ] ],
  "definitions" : {
    "EnaSrdSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EnaSrdEnabled" : {
          "type" : "boolean",
          "description" : "Indicates whether ENA Express is enabled for the network interface."
        },
        "EnaSrdUdpSpecification" : {
          "type" : "object",
          "additionalProperties" : False,
          "properties" : {
            "EnaSrdUdpEnabled" : {
              "type" : "boolean"
            }
          },
          "description" : "Configures ENA Express for UDP network traffic."
        }
      },
      "description" : "ENA Express uses AWS Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances. With ENA Express, you can communicate between two EC2 instances in the same subnet within the same account, or in different accounts. Both sending and receiving instances must have ENA Express enabled.\n To improve the reliability of network packet delivery, ENA Express reorders network packets on the receiving end by default. However, some UDP-based applications are designed to handle network packets that are out of order to reduce the overhead for packet delivery at the network layer. When ENA Express is enabled, you can specify whether UDP network traffic uses it."
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AttachNetworkInterface", "ec2:DescribeNetworkInterfaces", "ec2:ModifyNetworkInterfaceAttribute" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeNetworkInterfaces" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeNetworkInterfaces" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyNetworkInterfaceAttribute", "ec2:DescribeNetworkInterfaces", "ec2:AttachNetworkInterface", "ec2:DetachNetworkInterface" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DetachNetworkInterface", "ec2:DescribeNetworkInterfaces" ]
    }
  }
}
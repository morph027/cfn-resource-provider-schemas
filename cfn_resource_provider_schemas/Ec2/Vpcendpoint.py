SCHEMA = {
  "tagging" : {
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags", "ec2:DescribeVpcEndpoints" ],
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : True
  },
  "handlers" : {
    "read" : {
      "permissions" : [ "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "vpc-lattice:DescribeServiceNetworkVpcEndpointAssociation" ]
    },
    "create" : {
      "permissions" : [ "ec2:CreateVpcEndpoint", "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "vpc-lattice:CreateServiceNetworkVpcEndpointAssociation", "vpc-lattice:DescribeServiceNetworkVpcEndpointAssociation", "ec2:CreateTags", "ec2:DeleteTags", "vpce:AllowMultiRegion" ],
      "timeoutInMinutes" : 210
    },
    "update" : {
      "permissions" : [ "ec2:ModifyVpcEndpoint", "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "vpc-lattice:CreateServiceNetworkVpcEndpointAssociation", "vpc-lattice:DescribeServiceNetworkVpcEndpointAssociation", "ec2:CreateTags", "ec2:DeleteTags", "vpce:AllowMultiRegion" ],
      "timeoutInMinutes" : 210
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "vpc-lattice:DescribeServiceNetworkVpcEndpointAssociation" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteVpcEndpoints", "ec2:DescribeVpcEndpoints", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "vpc-lattice:DescribeServiceNetworkVpcEndpointAssociation", "ec2:CreateTags", "ec2:DeleteTags", "vpce:AllowMultiRegion" ],
      "timeoutInMinutes" : 210
    }
  },
  "typeName" : "AWS::EC2::VPCEndpoint",
  "readOnlyProperties" : [ "/properties/NetworkInterfaceIds", "/properties/CreationTimestamp", "/properties/DnsEntries", "/properties/Id" ],
  "description" : "Specifies a VPC endpoint. A VPC endpoint provides a private connection between your VPC and an endpoint service. You can use an endpoint service provided by AWS, an MKT Partner, or another AWS accounts in your organization. For more information, see the [User Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/).\n An endpoint of type ``Interface`` establishes connections between the subnets in your VPC and an AWS-service, your own service, or a service hosted by another AWS-account. With an interface VPC endpoint, you specify the subnets in which to create the endpoint and the security groups to associate with the endpoint network interfaces.\n An endpoint of type ``gateway`` serves as a target for a route in your route table for traffic destined for S3 or DDB. You can specify an endpoint policy for the endpoint, which controls access to the service from your VPC. You can also specify the VPC route tables that use the endpoint. For more information about connectivity to S3, see [Why can't I connect to an S3 bucket using a gateway VPC endpoint?](https://docs.aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint) \n An endpoint of type ``GatewayLoadBalancer`` provides private connectivity between your VPC and virtual appliances from a service provider.",
  "createOnlyProperties" : [ "/properties/ServiceName", "/properties/VpcEndpointType", "/properties/VpcId", "/properties/ServiceNetworkArn", "/properties/ResourceConfigurationArn", "/properties/ServiceRegion" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Id" ],
  "definitions" : {
    "DnsOptionsSpecification" : {
      "description" : "Describes the DNS options for an endpoint.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "PrivateDnsOnlyForInboundResolverEndpoint" : {
          "description" : "Indicates whether to enable private DNS only for inbound endpoints. This option is available only for services that support both gateway and interface endpoints. It routes traffic that originates from the VPC to the gateway endpoint and traffic that originates from on-premises to the interface endpoint.",
          "type" : "string",
          "enum" : [ "OnlyInboundResolver", "AllResolvers", "NotSpecified" ]
        },
        "DnsRecordIpType" : {
          "description" : "The DNS records created for the endpoint.",
          "type" : "string",
          "enum" : [ "ipv4", "ipv6", "dualstack", "service-defined", "not-specified" ]
        }
      }
    },
    "Tag" : {
      "description" : "Describes a tag.",
      "additionalProperties" : False,
      "type" : "object",
      "properties" : {
        "Value" : {
          "description" : "The value of the tag.\n Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.",
          "type" : "string"
        },
        "Key" : {
          "description" : "The key of the tag.\n Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with ``aws:``.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "PrivateDnsEnabled" : {
      "description" : "Indicate whether to associate a private hosted zone with the specified VPC. The private hosted zone contains a record set for the default public DNS name for the service for the Region (for example, ``kinesis.us-east-1.amazonaws.com``), which resolves to the private IP addresses of the endpoint network interfaces in the VPC. This enables you to make requests to the default public DNS name for the service instead of the public DNS names that are automatically generated by the VPC endpoint service.\n To use a private hosted zone, you must set the following VPC attributes to ``True``: ``enableDnsHostnames`` and ``enableDnsSupport``.\n This property is supported only for interface endpoints.\n Default: ``False``",
      "type" : "boolean"
    },
    "IpAddressType" : {
      "description" : "The supported IP address types.",
      "type" : "string",
      "enum" : [ "ipv4", "ipv6", "dualstack", "not-specified" ]
    },
    "ServiceRegion" : {
      "description" : "",
      "type" : "string"
    },
    "CreationTimestamp" : {
      "description" : "",
      "type" : "string"
    },
    "DnsOptions" : {
      "description" : "Describes the DNS options for an endpoint.",
      "$ref" : "#/definitions/DnsOptionsSpecification"
    },
    "NetworkInterfaceIds" : {
      "uniqueItems" : False,
      "description" : "",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "DnsEntries" : {
      "uniqueItems" : False,
      "description" : "",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "ResourceConfigurationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the resource configuration.",
      "type" : "string"
    },
    "SecurityGroupIds" : {
      "uniqueItems" : True,
      "description" : "The IDs of the security groups to associate with the endpoint network interfaces. If this parameter is not specified, we use the default security group for the VPC. Security groups are supported only for interface endpoints.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "anyOf" : [ {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::SecurityGroup",
            "propertyPath" : "/properties/GroupId"
          }
        }, {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::SecurityGroup",
            "propertyPath" : "/properties/Id"
          }
        }, {
          "relationshipRef" : {
            "typeName" : "AWS::EC2::VPC",
            "propertyPath" : "/properties/DefaultSecurityGroup"
          }
        } ],
        "type" : "string"
      }
    },
    "SubnetIds" : {
      "uniqueItems" : True,
      "description" : "The IDs of the subnets in which to create endpoint network interfaces. You must specify this property for an interface endpoint or a Gateway Load Balancer endpoint. You can't specify this property for a gateway endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "relationshipRef" : {
          "typeName" : "AWS::EC2::Subnet",
          "propertyPath" : "/properties/SubnetId"
        },
        "type" : "string"
      }
    },
    "ServiceNetworkArn" : {
      "description" : "The Amazon Resource Name (ARN) of the service network.",
      "type" : "string"
    },
    "VpcId" : {
      "description" : "The ID of the VPC.",
      "type" : "string"
    },
    "RouteTableIds" : {
      "uniqueItems" : True,
      "description" : "The IDs of the route tables. Routing is supported only for gateway endpoints.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "relationshipRef" : {
          "typeName" : "AWS::EC2::RouteTable",
          "propertyPath" : "/properties/RouteTableId"
        },
        "type" : "string"
      }
    },
    "ServiceName" : {
      "description" : "The name of the endpoint service.",
      "type" : "string"
    },
    "PolicyDocument" : {
      "description" : "An endpoint policy, which controls access to the service from the VPC. The default endpoint policy allows full access to the service. Endpoint policies are supported only for gateway and interface endpoints.\n For CloudFormation templates in YAML, you can provide the policy in JSON or YAML format. For example, if you have a JSON policy, you can convert it to YAML before including it in the YAML template, and CFNlong converts the policy to JSON format before calling the API actions for privatelink. Alternatively, you can include the JSON directly in the YAML, as shown in the following ``Properties`` section:\n ``Properties: VpcEndpointType: 'Interface' ServiceName: !Sub 'com.amazonaws.${AWS::Region}.logs' PolicyDocument: '{ \"Version\":\"2012-10-17\", \"Statement\": [{ \"Effect\":\"Allow\", \"Principal\":\"*\", \"Action\":[\"logs:Describe*\",\"logs:Get*\",\"logs:List*\",\"logs:FilterLogEvents\"], \"Resource\":\"*\" }] }'``",
      "type" : [ "string", "object" ]
    },
    "VpcEndpointType" : {
      "description" : "The type of endpoint.\n Default: Gateway",
      "type" : "string",
      "enum" : [ "Interface", "Gateway", "GatewayLoadBalancer", "ServiceNetwork", "Resource" ]
    },
    "Id" : {
      "description" : "",
      "type" : "string"
    },
    "Tags" : {
      "uniqueItems" : False,
      "description" : "The tags to associate with the endpoint.",
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "VpcId" ]
}
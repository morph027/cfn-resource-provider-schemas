SCHEMA = {
  "typeName" : "AWS::EC2::VPCEndpointService",
  "description" : "Resource Type definition for AWS::EC2::VPCEndpointService",
  "additionalProperties" : False,
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "IpAddressType" : {
      "type" : "string",
      "enum" : [ "ipv4", "ipv6" ]
    }
  },
  "properties" : {
    "NetworkLoadBalancerArns" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string",
        "relationshipRef" : {
          "typeName" : "AWS::ElasticLoadBalancingV2::LoadBalancer",
          "propertyPath" : "/properties/LoadBalancerArn"
        }
      }
    },
    "ContributorInsightsEnabled" : {
      "type" : "boolean"
    },
    "PayerResponsibility" : {
      "type" : "string"
    },
    "ServiceId" : {
      "type" : "string"
    },
    "AcceptanceRequired" : {
      "type" : "boolean"
    },
    "GatewayLoadBalancerArns" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "type" : "array",
      "description" : "The tags to add to the VPC endpoint service.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SupportedIpAddressTypes" : {
      "type" : "array",
      "description" : "Specify which Ip Address types are supported for VPC endpoint service.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/IpAddressType"
      }
    },
    "SupportedRegions" : {
      "type" : "array",
      "description" : "The Regions from which service consumers can access the service.",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    }
  },
  "primaryIdentifier" : [ "/properties/ServiceId" ],
  "readOnlyProperties" : [ "/properties/ServiceId" ],
  "writeOnlyProperties" : [ "/properties/ContributorInsightsEnabled" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateVpcEndpointServiceConfiguration", "ec2:ModifyVpcEndpointServicePayerResponsibility", "cloudwatch:ListManagedInsightRules", "cloudwatch:DeleteInsightRules", "cloudwatch:PutManagedInsightRules", "ec2:DescribeVpcEndpointServiceConfigurations", "vpce:AllowMultiRegion", "ec2:CreateTags" ]
    },
    "update" : {
      "permissions" : [ "ec2:ModifyVpcEndpointServiceConfiguration", "ec2:DescribeVpcEndpointServiceConfigurations", "ec2:ModifyVpcEndpointServicePayerResponsibility", "cloudwatch:ListManagedInsightRules", "cloudwatch:DeleteInsightRules", "cloudwatch:PutManagedInsightRules", "ec2:CreateTags", "ec2:DeleteTags", "vpce:AllowMultiRegion" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVpcEndpointServiceConfigurations", "cloudwatch:ListManagedInsightRules" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteVpcEndpointServiceConfigurations", "ec2:DescribeVpcEndpointServiceConfigurations", "cloudwatch:ListManagedInsightRules", "cloudwatch:DeleteInsightRules", "ec2:DeleteTags", "vpce:AllowMultiRegion" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVpcEndpointServiceConfigurations", "cloudwatch:ListManagedInsightRules" ]
    }
  }
}
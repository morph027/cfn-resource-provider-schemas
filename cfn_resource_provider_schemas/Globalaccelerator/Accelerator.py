SCHEMA = {
  "typeName" : "AWS::GlobalAccelerator::Accelerator",
  "description" : "Resource Type definition for AWS::GlobalAccelerator::Accelerator",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-globalaccelerator",
  "definitions" : {
    "Tag" : {
      "description" : "Tag is a key-value pair associated with accelerator.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "Key of the tag. Value can be 1 to 127 characters.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "description" : "Value for the tag. Value can be 1 to 255 characters.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "IpAddress" : {
      "pattern" : "^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$",
      "description" : "An IPV4 address",
      "type" : "string"
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of accelerator.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]{0,64}$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "IpAddressType" : {
      "description" : "IP Address type.",
      "type" : "string",
      "default" : "IPV4",
      "enum" : [ "IPV4", "DUAL_STACK" ]
    },
    "IpAddresses" : {
      "description" : "The IP addresses from BYOIP Prefix pool.",
      "default" : None,
      "insertionOrder" : True,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/IpAddress"
      }
    },
    "Enabled" : {
      "description" : "Indicates whether an accelerator is enabled. The value is True or False.",
      "default" : True,
      "type" : "boolean"
    },
    "DnsName" : {
      "description" : "The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.",
      "type" : "string"
    },
    "Ipv4Addresses" : {
      "description" : "The IPv4 addresses assigned to the accelerator.",
      "insertionOrder" : True,
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "Ipv6Addresses" : {
      "description" : "The IPv6 addresses assigned if the accelerator is dualstack",
      "default" : None,
      "insertionOrder" : True,
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "DualStackDnsName" : {
      "description" : "The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.",
      "type" : "string"
    },
    "AcceleratorArn" : {
      "description" : "The Amazon Resource Name (ARN) of the accelerator.",
      "type" : "string"
    },
    "Tags" : {
      "insertionOrder" : True,
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "required" : [ "Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "globalaccelerator:CreateAccelerator", "globalaccelerator:DescribeAccelerator", "globalaccelerator:TagResource" ]
    },
    "read" : {
      "permissions" : [ "globalaccelerator:DescribeAccelerator" ]
    },
    "update" : {
      "permissions" : [ "globalaccelerator:UpdateAccelerator", "globalaccelerator:TagResource", "globalaccelerator:UntagResource", "globalaccelerator:DescribeAccelerator" ]
    },
    "delete" : {
      "permissions" : [ "globalaccelerator:UpdateAccelerator", "globalaccelerator:DeleteAccelerator", "globalaccelerator:DescribeAccelerator" ]
    },
    "list" : {
      "permissions" : [ "globalaccelerator:ListAccelerators" ]
    }
  },
  "readOnlyProperties" : [ "/properties/AcceleratorArn", "/properties/DnsName", "/properties/Ipv4Addresses", "/properties/Ipv6Addresses", "/properties/DualStackDnsName" ],
  "primaryIdentifier" : [ "/properties/AcceleratorArn" ],
  "additionalProperties" : False
}
SCHEMA = {
  "typeName" : "AWS::EMRContainers::VirtualCluster",
  "description" : "Resource Schema of AWS::EMRContainers::VirtualCluster Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "ContainerProvider" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "description" : "The type of the container provider",
          "type" : "string"
        },
        "Id" : {
          "description" : "The ID of the container cluster",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 100,
          "pattern" : "^[0-9A-Za-z][A-Za-z0-9\\-_]*"
        },
        "Info" : {
          "$ref" : "#/definitions/ContainerInfo"
        }
      },
      "required" : [ "Type", "Id", "Info" ]
    },
    "ContainerInfo" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EksInfo" : {
          "$ref" : "#/definitions/EksInfo"
        }
      },
      "required" : [ "EksInfo" ]
    },
    "EksInfo" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Namespace" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 63,
          "pattern" : "[a-z0-9]([-a-z0-9]*[a-z0-9])?"
        }
      },
      "required" : [ "Namespace" ]
    },
    "Tag" : {
      "description" : "An arbitrary set of tags (key-value pairs) for this virtual cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "ContainerProvider" : {
      "description" : "Container provider of the virtual cluster.",
      "$ref" : "#/definitions/ContainerProvider"
    },
    "Id" : {
      "description" : "Id of the virtual cluster.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Name" : {
      "description" : "Name of the virtual cluster.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "[\\.\\-_/#A-Za-z0-9]+"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this virtual cluster.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SecurityConfigurationId" : {
      "description" : "The ID of the security configuration.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "[0-9a-z]+"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "ContainerProvider" ],
  "createOnlyProperties" : [ "/properties/ContainerProvider", "/properties/Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "emr-containers:TagResource", "emr-containers:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "emr-containers:CreateVirtualCluster", "emr-containers:TagResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "emr-containers:DescribeVirtualCluster" ]
    },
    "delete" : {
      "permissions" : [ "emr-containers:DeleteVirtualCluster", "emr-containers:DescribeVirtualCluster" ]
    },
    "list" : {
      "permissions" : [ "emr-containers:ListVirtualClusters" ]
    },
    "update" : {
      "permissions" : [ "emr-containers:DescribeVirtualCluster", "emr-containers:ListTagsForResource", "emr-containers:TagResource", "emr-containers:UntagResource" ]
    }
  }
}
SCHEMA = {
  "typeName" : "AWS::S3Outposts::Endpoint",
  "description" : "Resource Type Definition for AWS::S3Outposts::Endpoint",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3outposts.git",
  "definitions" : {
    "iso8601UTC" : {
      "description" : "The date value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    },
    "NetworkInterface" : {
      "description" : "The container for the network interface.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "NetworkInterfaceId" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 100
        }
      },
      "required" : [ "NetworkInterfaceId" ]
    },
    "FailedReason" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ErrorCode" : {
          "type" : "string",
          "description" : "The failure code, if any, for a create or delete endpoint operation."
        },
        "Message" : {
          "type" : "string",
          "description" : "Additional error details describing the endpoint failure and recommended action."
        }
      }
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the endpoint.",
      "minLength" : 5,
      "maxLength" : 500,
      "type" : "string",
      "pattern" : "^arn:[^:]+:s3-outposts:[a-zA-Z0-9\\-]+:\\d{12}:outpost\\/[^:]+\\/endpoint/[a-zA-Z0-9]{19}$"
    },
    "CidrBlock" : {
      "description" : "The VPC CIDR committed by this endpoint.",
      "minLength" : 1,
      "maxLength" : 20,
      "type" : "string"
    },
    "CreationTime" : {
      "description" : "The time the endpoint was created.",
      "$ref" : "#/definitions/iso8601UTC"
    },
    "Id" : {
      "description" : "The ID of the endpoint.",
      "minLength" : 5,
      "maxLength" : 500,
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9]{19}$"
    },
    "NetworkInterfaces" : {
      "description" : "The network interfaces of the endpoint.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/NetworkInterface"
      }
    },
    "OutpostId" : {
      "description" : "The id of the customer outpost on which the bucket resides.",
      "pattern" : "^(op-[a-f0-9]{17}|\\d{12}|ec2)$",
      "type" : "string"
    },
    "SecurityGroupId" : {
      "description" : "The ID of the security group to use with the endpoint.",
      "minLength" : 1,
      "maxLength" : 100,
      "type" : "string",
      "pattern" : "^sg-([0-9a-f]{8}|[0-9a-f]{17})$"
    },
    "Status" : {
      "type" : "string",
      "enum" : [ "Available", "Pending", "Deleting", "Create_Failed", "Delete_Failed" ]
    },
    "SubnetId" : {
      "description" : "The ID of the subnet in the selected VPC. The subnet must belong to the Outpost.",
      "minLength" : 1,
      "maxLength" : 100,
      "type" : "string",
      "pattern" : "^subnet-([0-9a-f]{8}|[0-9a-f]{17})$"
    },
    "AccessType" : {
      "description" : "The type of access for the on-premise network connectivity for the Outpost endpoint. To access endpoint from an on-premises network, you must specify the access type and provide the customer owned Ipv4 pool.",
      "type" : "string",
      "enum" : [ "CustomerOwnedIp", "Private" ],
      "default" : "Private"
    },
    "CustomerOwnedIpv4Pool" : {
      "description" : "The ID of the customer-owned IPv4 pool for the Endpoint. IP addresses will be allocated from this pool for the endpoint.",
      "type" : "string",
      "pattern" : "^ipv4pool-coip-([0-9a-f]{17})$"
    },
    "FailedReason" : {
      "description" : "The failure reason, if any, for a create or delete endpoint operation.",
      "$ref" : "#/definitions/FailedReason"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "OutpostId", "SecurityGroupId", "SubnetId" ],
  "createOnlyProperties" : [ "/properties/OutpostId", "/properties/SecurityGroupId", "/properties/SubnetId", "/properties/AccessType", "/properties/CustomerOwnedIpv4Pool" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CidrBlock", "/properties/CreationTime", "/properties/Id", "/properties/NetworkInterfaces", "/properties/Status" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3-outposts:CreateEndpoint" ]
    },
    "read" : {
      "permissions" : [ "s3-outposts:ListEndpoints" ]
    },
    "delete" : {
      "permissions" : [ "s3-outposts:DeleteEndpoint" ]
    },
    "list" : {
      "permissions" : [ "s3-outposts:ListEndpoints" ]
    }
  }
}
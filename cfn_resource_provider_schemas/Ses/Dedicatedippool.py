SCHEMA = {
  "typeName" : "AWS::SES::DedicatedIpPool",
  "description" : "Resource Type definition for AWS::SES::DedicatedIpPool",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ses.git",
  "properties" : {
    "PoolName" : {
      "type" : "string",
      "description" : "The name of the dedicated IP pool.",
      "pattern" : "^[a-z0-9_-]{0,64}$"
    },
    "ScalingMode" : {
      "type" : "string",
      "description" : "Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.",
      "pattern" : "^(STANDARD|MANAGED)$"
    }
  },
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/PoolName" ],
  "conditionalCreateOnlyProperties" : [ "/properties/ScalingMode" ],
  "primaryIdentifier" : [ "/properties/PoolName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ses:CreateDedicatedIpPool", "ses:GetDedicatedIpPool", "ses:GetDedicatedIps" ]
    },
    "read" : {
      "permissions" : [ "ses:GetDedicatedIpPool", "ses:GetDedicatedIps" ]
    },
    "update" : {
      "permissions" : [ "ses:PutDedicatedIpPoolScalingAttributes", "ses:GetDedicatedIpPool" ]
    },
    "delete" : {
      "permissions" : [ "ses:DeleteDedicatedIpPool" ]
    },
    "list" : {
      "permissions" : [ "ses:ListDedicatedIpPools" ]
    }
  }
}